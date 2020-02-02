# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository.Gtk import Box,Template


@Template(filename='LabeledComponent.glade')
class LabeledComponent(Box):
    __gtype_name__='LabeledComponent'
    Label = Template.Child()
    Header = Template.Child(internal=True)
    Main  = Template.Child(internal=True)
    Footer = Template.Child(internal=True)
    def __new__(cls,*args,**kwargs):
        print ("NEW")
        result = Box.__new__(cls,*args,**kwargs)
        return result
    def addHeader(self,comp):
        self.Header.add(comp)
        pass
    def set_label(self,text):
        self.Label.set_label(text)
        pass
    pass

if __name__=='__main__':

    lc = LabeledComponent()
