# encoding: utf-8
from PyQt4.QtGui import QApplication, QMessageBox, QSplashScreen
from PyQt4.QtCore import SIGNAL

from os.path import join, exists, isdir, isabs, basename, abspath

from os import getpid, unlink, getcwd
from prymatex.lib.deco import printtime
import sys
from time import time

from prymatex.lib.exceptions import AlreadyRunningError
from prymatex.lib.textmate import load_textmate_bundles, load_textmate_themes
        
        
class PMXApplication(QApplication):
    
    __config = None
    __res_mngr = None
    
    @printtime
    def __init__(self, arguments):
        '''
        Inicialización de la aplicación.
        '''
        QApplication.__init__(self, arguments)
        
        from prymatex.optargs import parser
        options, args = parser.parse_args(arguments)
        files_to_open = args[1:]
        
        self.init_application_params()
        
        self.init_resources()
        self.splash = QSplashScreen(self.res_mngr.getPixmap('Prymatex_Splash.png'))
        self.splash.show()
        
        self.setWindowIcon(self.res_mngr.getIcon('Prymatex_Logo.png'))
        
        self.check_single_instance()
        
        # Settings
        self.init_config()
        
        # Bundles and Stuff
        self.load_texmate_themes()
        self.load_texmate_bundles()
        
        
        from prymatex.gui.mainwindow import PMXMainWindow
        self.main_window = PMXMainWindow()
        self.splash.finish(self.main_window)
        self.main_window.show()
        
        self.connect(self, SIGNAL('aboutToQuit()'), self.cleanup)
        self.connect(self, SIGNAL('aboutToQuit()'), self.save_config)
    
    def init_application_params(self):
        self.setApplicationName("Prymatex Text Editor")
        self.setApplicationVersion("0.1") # hg stuff?
        self.setOrganizationDomain("org")
        self.setOrganizationName("Xurix")
        self.projectUrl = 'http://code.google.com/p/prymatex'    
    
    @property
    def lock_filename(self):
        return join(self.res_mngr.path, 'LOCK') 
    
    def cleanup(self):
        try:
            unlink(self.lock_filename)
        except:
            pass
    
    def save_config(self):
        print "Save config"
        self.config.save()
    
    def init_resources(self):
        if not self.__res_mngr:
            from prymatex.resmgr import resource_manager
            self.__res_mngr = resource_manager
        
    def init_config(self):
        if not self.__config:
            from prymatex.conf import settings, PRYMATEX_SETTINGS_FILE
            from prymatex.lib.i18n import ugettext as _
            self.__config = settings
            # Se pudo cargar la configuración???
#            if not self.__config.loaded:
#                QMessageBox.information(None, _("Configuration Defaults"), _("""
#                <p>The configuration file <i><b>%s</b></i> was not found on <i>%s</i> application
#                directory.</p><p> A default settings file has been creates and will
#                be saved when you close this app. If you belive this is a mistake
#                please check the file or its contents.</p>
#                
#                """, basename(PRYMATEX_SETTINGS_FILE), self.applicationName()))
        
    @property
    def config(self):
        '''
        Retorna un objeto que soporta xxx.yyy.zzz
        y que puede propagar señales ante edición.
        '''
        return self.__config
        
    @property
    def res_mngr(self):
        '''
        Retorna el administrador de recursos
        '''
        return self.__res_mngr
    
    def deferred_load_texmate_bundles(self):
        '''
        Crea una lista de los paths abslutos de donde se cargan
        bundles y lanza un hilo para cargarlos.
        '''
        from prymatex.lib.textmate.loader import PMXBundleLoaderThread
        print "iniciando hilo de bundles con", self.config.TEXTMATE_BUNDLES_PATHS
        path_list = []
        for dirname in self.config.TEXTMATE_BUNDLES_PATHS:
            if isdir(dirname):
                if not isabs(dirname):
                    dirname = join(getcwd(), dirname)
                path_list.append(dirname)
        self.bundle_thread = PMXBundleLoaderThread(path_list, self)
        self.bundle_thread.start()
    
    def load_texmate_themes(self):
        '''
        Load textmate Bundles and Themes
        '''
        from prymatex.lib.i18n import ugettext as _
        if not all(map(lambda x: hasattr(self.config, x), ('TEXTMATE_THEMES_PATHS',
                                                           'TEXTMATE_BUNDLES_PATHS' ))):
            QMessageBox.critical(self, _("Fatal Error"), 
                                 _("No bundle dirs have been found in config file."))
        
        self.splash.showMessage(_("Loading themes..."))
        themes = 0
        for dirname in self.config.TEXTMATE_THEMES_PATHS:
            if isdir(dirname):
                if not isabs(dirname):
                    dirname = join(getcwd(), dirname)
                themes += load_textmate_themes(dirname)
                
            else:
                print("El directorio de temas %s no existe" % dirname)
            
        self.splash.showMessage(_("%d themes loaded", themes))
        QApplication.processEvents()
    
    # Decorador para imprimir cuanto tarda
    @printtime
    def load_texmate_bundles(self):
        from prymatex.lib.i18n import ugettext as _
        bundles = 0
        splash = self.splash
        def before_load_callback(counter, total, name):
            progress = (float(counter) / total) * 100
            splash.showMessage(_("Loading bundle %s\n%4d of %4d (%.d%%)", 
                                 name, counter, total, progress))
            QApplication.processEvents()
            
        for dirname in self.config.TEXTMATE_BUNDLES_PATHS:
            self.splash.showMessage(_("Loading bundles..."))
            if isdir(dirname):
                if not isabs(dirname):
                    dirname = join(getcwd(), dirname) 
                bundles += load_textmate_bundles(dirname, before_load_callback)
            else:
                print("El directorio de temas %s no existe" % dirname)
        QApplication.processEvents()
        
    def check_single_instance(self):
        '''
        Intenta trabajar con una sola instancia
        '''
        from prymatex.lib import os
        if exists(self.lock_filename):
            f = open(self.lock_filename)
            pid = int(f.read())
            f.close()
            print "Esta?", pid in os.pid_proc_dict()
            if pid in os.pid_proc_dict():
                from prymatex.lib.i18n import ugettext as _
                print "PID Existente"
                QMessageBox.critical(None, _('Application Already Running'),
                                     _('''%s seems to be runnig. Please
                                     close the other instance.''', self.applicationName()),
                                     QMessageBox.Ok)
                raise AlreadyRunningError(pid)
            
        else:
            f = open(self.lock_filename, 'w')
            f.write('%s' % getpid())
            f.close()
    
    
        
