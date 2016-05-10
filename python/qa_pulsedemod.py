#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from pulsedemod import pulsedemod

class qa_pulsedemod (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        bit_timeout = (0,) * 2000
        bit_pause = (0.,) * 30
        zero_bit = bit_pause  + (1.,) * 500
        one_bit = bit_pause  + (1.,) * 220
        in_bits = bit_timeout  + zero_bit + one_bit + one_bit  + one_bit + bit_timeout
        #print (in_bits)
        source = blocks.vector_source_f(in_bits)
        sink = pulsedemod();
        self.tb.connect(source,sink)
        self.tb.run ()
        # check data

    def test_002_t (self):
		#test the end_sample methods
		stream =  pulsedemod()
		stream.end_sample(0,1000)
		stream.end_sample(1,150)

    def set_sample_rate(self,samp_rate):
        print "Setting sample rate to %i" % samp_rate
	stream =  pulsedemod()
	stream.set_sample_rate(44000)

if __name__ == '__main__':
    gr_unittest.run(qa_pulsedemod, "qa_pulsedemod.xml")
