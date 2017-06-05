# Copyright (C) 2016 YouCompleteMe contributors
#
# This file is part of YouCompleteMe.
#
# YouCompleteMe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# YouCompleteMe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with YouCompleteMe.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
# Not installing aliases from python-future; it's unreliable and slow.
from builtins import *  # noqa

from icm.tests.test_utils import ( MockVimModule, MockVimBuffers, VimBuffer )
MockVimModule()

from hamcrest import assert_that, equal_to
from mock import patch

from icm.tests import YouCompleteMeInstance


@YouCompleteMeInstance( { 'extra_conf_vim_data': [ 'tempname()' ] } )
def SendCommandRequest_test( ycm ):
  current_buffer = VimBuffer( 'buffer' )
  with MockVimBuffers( [ current_buffer ], current_buffer ):
    with patch( 'icm.youcompleteme.SendCommandRequest' ) as send_request:
      ycm.SendCommandRequest( [ 'GoTo' ], 'python' )
      send_request.assert_called_once_with(
        [ 'GoTo' ], 'python', { 'extra_conf_data': {
          'tempname()': '_TEMP_FILE_' } }
      )
    with patch( 'icm.client.base_request.JsonFromFuture',
                return_value = 'Some response' ):
      assert_that(
        ycm.SendCommandRequest( [ 'GoTo' ], 'python' ),
        equal_to( 'Some response' )
      )
