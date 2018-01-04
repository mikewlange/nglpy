 ##############################################################################
 # Software License Agreement (BSD License)                                   #
 #                                                                            #
 # Copyright 2014 University of Utah                                          #
 # Scientific Computing and Imaging Institute                                 #
 # 72 S Central Campus Drive, Room 3750                                       #
 # Salt Lake City, UT 84112                                                   #
 #                                                                            #
 # THE BSD LICENSE                                                            #
 #                                                                            #
 # Redistribution and use in source and binary forms, with or without         #
 # modification, are permitted provided that the following conditions         #
 # are met:                                                                   #
 #                                                                            #
 # 1. Redistributions of source code must retain the above copyright          #
 #    notice, this list of conditions and the following disclaimer.           #
 # 2. Redistributions in binary form must reproduce the above copyright       #
 #    notice, this list of conditions and the following disclaimer in the     #
 #    documentation and/or other materials provided with the distribution.    #
 # 3. Neither the name of the copyright holder nor the names of its           #
 #    contributors may be used to endorse or promote products derived         #
 #    from this software without specific prior written permission.           #
 #                                                                            #
 # THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR       #
 # IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES  #
 # OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.    #
 # IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,           #
 # INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT   #
 # NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  #
 # DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY      #
 # THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT        #
 # (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF   #
 # THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.          #
 ##############################################################################
"""
      Setup script for pyerg, a wrapper library for the C++ implementataion of
      the neigbhorhood graph library (NGL).
"""

from distutils.core import setup, Extension

FILES = ['ngl.i', 'GraphStructure.cpp', 'UnionFind.cpp']

setup(name='pyerg',
      packages=['pyerg'],
      version='0.1',
      description='A wrapper library for exposing the C++ neighborhood graph '
                  + 'library (NGL) for computing empty region graphs to python',
      author = 'Dan Maljovec',
      author_email = 'maljovec002@gmail.com',
      url = 'https://github.com/maljovec/pyerg',
      download_url = 'https://github.com/maljovec/pyerg/archive/0.1.tar.gz',
      keywords = ['geometry', 'graph', 'empty region graph'],
      classifiers = [],
      ext_modules=[Extension('_ngl', FILES,
                             swig_opts=['-c++'],
                             extra_compile_args=['-std=c++11'])])
