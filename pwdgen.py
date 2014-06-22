#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import hashlib

class PasswordGenerator:
    
    def generate_password (self, widget):
      master_password = self.master_password_entry.get_text()
      salt_domain = self.domain_salt_entry.get_text()
      offset = self.offset_spinner.get_value_as_int()
      length = self.length_spinner.get_value_as_int()
      
      digest = hashlib.md5("%s%s" % (master_password, salt_domain)).hexdigest()
      raw_password = digest.encode("base64").strip()
      
      mirror_password = raw_password * ((offset+length) / 44 + 1)
      
      password = mirror_password[offset:offset+length]
      
      clipboard = gtk.Clipboard()
      clipboard.set_text(password, len=-1)
    
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_title("Password Generator 0.1")

        main_vbox = gtk.VBox(False, 5)
        main_vbox.set_border_width(10)
        window.add(main_vbox)

        frame = gtk.Frame("")
        main_vbox.pack_start(frame, True, True, 0)
        
  
        button = gtk.Button("Copy to Clipboard")
        button.connect("clicked", self.generate_password)
        main_vbox.pack_start(button, False, True, 0)
        
        vbox = gtk.VBox(False, 0)
        vbox.set_border_width(5)
        frame.add(vbox)

        hbox2 = gtk.HBox(False, 0)
        vbox.pack_start(hbox2, True, True, 5)
        
        vbox0 = gtk.VBox(False, 0)
        hbox2.pack_start(vbox0, True, True, 5)
        
        label0 = gtk.Label("Master Password :")
        label0.set_alignment(0, 0.5)
        vbox0.pack_start(label0, False, True, 0)
        label0.show()
        
        self.master_password_entry = gtk.Entry()
        self.master_password_entry.set_visibility(False)
        vbox0.pack_start(self.master_password_entry, False, True, 0)
        self.master_password_entry.show()
        
        hbox = gtk.HBox(False, 0)
        vbox.pack_start(hbox, True, True, 5)
        
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)

        label = gtk.Label("Domain/Salt :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)
  
        self.domain_salt_entry = gtk.Entry()
        vbox2.pack_start(self.domain_salt_entry, False, True, 0)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
        label = gtk.Label("Offset :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)

        adj = gtk.Adjustment(1.0, 1.0, 99.0, 1.0, 1.0, 0.0)
        # FIXME: change length when offset is growing big
        #        offset + length - 1 > 44
        # adj.connect("value_changed", self.offset_length_changed)
        self.offset_spinner = gtk.SpinButton(adj, 0, 0)
        self.offset_spinner.set_wrap(True)
        vbox2.pack_start(self.offset_spinner, False, True, 0)
  
        vbox2 = gtk.VBox(False, 0)
        hbox.pack_start(vbox2, True, True, 5)
  
        label = gtk.Label("Length :")
        label.set_alignment(0, 0.5)
        vbox2.pack_start(label, False, True, 0)
  
        adj = gtk.Adjustment(8, 1.0, 99.0, 1.0, 1.0, 0.0)
        # FIXME: change length when offset is growing big
        #        offset + length - 1 > 44
        # adj.connect("value_changed", self.offset_length_changed)
        self.length_spinner = gtk.SpinButton(adj, 0, 0)
        self.length_spinner.set_wrap(True)
        self.length_spinner.set_size_request(55, -1)
        vbox2.pack_start(self.length_spinner, False, True, 0)
        
        window.show_all()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    PasswordGenerator()
    main()
