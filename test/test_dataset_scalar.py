##############################################################################
# Copyright by The HDF Group.                                                #
# All rights reserved.                                                       #
#                                                                            #
# This file is part of H5Serv (HDF5 REST Server) Service, Libraries and      #
# Utilities.  The full HDF5 REST Server copyright notice, including          #
# terms governing use, modification, and redistribution, is contained in     #
# the file COPYING, which can be found at the root of the source code        #
# distribution tree.  If you do not have access to this file, you may        #
# request a copy from help@hdfgroup.org.                                     #
##############################################################################

import numpy as np
import math

import config

if config.get("use_h5py"):
    import h5py
else:
    import h5pyd as h5py
    
from common import ut, TestCase

        
class TestScalarDataset(TestCase):
    def test_scalar_dset(self):
        filename = self.getFileName("scalar_dset")
        print("filename:", filename)
        f = h5py.File(filename, "w")     
        
        dset = f.create_dataset('scalar', data=42, dtype='i8')
 
        val = dset[()]
        print("val:", val)
        self.assertEqual(dset.shape, ())
        
        self.assertEqual(dset.file.filename, filename)
        f.close()
    
    
if __name__ == '__main__':
    ut.main()