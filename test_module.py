from LabeledComponent import LabeledComponent



def lcadaptor(self,adapter,widget,reason):
    print("Found adapter %s %s %s" % (adapter,widget,reason))
    pass


if __name__=="__main__":
    import gi
    gi.require_version('Gtk', '3.0')
    gi.require_version('Gladeui', '2.0')
    from gi.repository import Gladeui,GObject
    from gi import types
    pass

