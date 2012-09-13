#!/usr/bin/env python

'''
dvd_player.py - Example of a simple object.

An implementation of an idealised dvd player, for learning purposes.

Author: Eric Saunders
January 2011
'''

class DVDPlayer(object):

    def __init__(self):
        self.current_disc = None


    def insert_disc(self, dvd):
        if self.current_disc:
            name = self.current_disc.name
            print 'Try taking the current disc ("%s") out first, numbskull.' % name

        else:
            print "Slurp ... CLICK ... Chug chug chug ..."
            self.current_disc = dvd


    def eject(self):
        if self.current_disc:
            print "CLICK ... grrrrr ... POP ..."
            print '[the DVD "%s" glides out of the player.]' % self.current_disc.name

            disc_to_return = self.current_disc
            self.current_disc = None

            return disc_to_return


        else:
            print "Having trouble ejecting a disc that isn't there, eh?"


    def play(self):
        if self.current_disc:
            content_length = len(self.current_disc.content)
            tv_screen_width = content_length + 4
            print ""
            print " " + "-" * tv_screen_width
            print "|  " + self.current_disc.content + "  |"
            print "|" + " " * tv_screen_width + "|"
            print "|" + " [FIN]" + " " * (tv_screen_width - 6) + "|"
            print "-" * tv_screen_width
        else:
            print "Play? With what? You idiot. INSERT A DISC FIRST, MORON."



    def get_disc_info(self):
        if self.current_disc:
            print "Current disc:", self.current_disc.name
            print "Running time: %s minutes" % self.current_disc.running_time

        else:
            print ("Do you find asking unanswerable questions a gratifying"
                   " experience? Do you? DO YOU?")


    def burn_disc(self):
        if self.current_disc:
            answer = raw_input('Current disc is "%s". Do you really want to record over this? '
                               % self.current_disc.name )

            if answer == 'n': return

            print "Activating video device..."
            print "Do stuff (hit enter to stop recording):"
            new_content = raw_input()
            self.current_disc.content = new_content

            print "DVD burning complete."

        else:
            print ("Go borrow the braincell from your moron cousin, come back"
                  " and try again. I'll wait.")


class DVD(object):

    def __init__(self, name, running_time, content):
        self.name         = name
        self.running_time = running_time
        self.content      = content


if __name__ == '__main__':
    dvd = DVD("Heathers", 103, "F*** me gently with a chainsaw!")
    player = DVDPlayer()
    player.insert_disc(dvd)
