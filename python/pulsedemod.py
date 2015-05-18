#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 kees Jongenburger
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class pulsedemod(gr.sync_block):
    """
    docstring for block pulsedemod
    """
    def __init__(self):
		gr.sync_block.__init__(self, name="pulsedemod", in_sig=[numpy.float32], out_sig=None)
		self.upcount=0
		self.downcount=0
		self.bits = ""

    def set_sample_rate(self,samp_rate):
        print "Setting sample rate to %i" % samp_rate

    def end_sample(self,value,count):
		if value == 1:
			if (count < 50):
				print "SKIP"
				return
			if (count < 200):
				self.bits  += "0"
			if (count > 210):
				self.bits += "1"
		if value == 0:
			if count > 600:
				print("BITS %s" % self.bits)
				self.bits = ""

    def work(self, input_items, output_items):
		in0 = input_items[0]
		for i in range(0, len(in0)):
			sample = in0[i]

			# do upcount
			if sample < 0.5 and self.upcount > 0:
				self.end_sample(1,self.upcount)
				self.upcount = 0
			if sample > 0.5:
				self.upcount += 1

			# do downcount
			if sample > 0.5 and self.downcount > 0:
				self.end_sample(0,self.downcount)
				self.downcount = 0
			if sample < 0.5:
				self.downcount += 1
		return len(input_items[0])
