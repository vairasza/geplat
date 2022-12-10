from gi.repository import GObject, Gedit
import time

class GEPLatApp(GObject.Object, Gedit.WindowActivatable):

    window = GObject.property(type=Gedit.Window)
    __gtype_name__ = "GEPLatPlugin"

    def __init__(self):
        GObject.Object.__init__(self)
        self.deletion_timer = 1.0

    def do_activate(self):
        print("plugin active")
        self.event_id = self.window.connect("key-release-event", self.on_key_release)

        return

    def do_deactivate(self):
        print("plugin deactivated")
        self.window.disconnect(self.event_id)

        return

    def do_update_state(self):
        pass

    def on_key_release(self, window, event):
        #character is already rendered in the document

        #wait set amount of time
        time.sleep(self.deletion_timer)

        #before deleting the character again
        doc = window.get_active_document()
        if doc is not None:
            doc.set_text("", -1)
        
        return