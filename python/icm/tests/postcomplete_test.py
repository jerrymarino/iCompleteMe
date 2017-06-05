# encoding: utf-8
#
# Copyright (C) 2015-2016 YouCompleteMe contributors
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

from icm.tests.test_utils import MockVimModule
MockVimModule()

import contextlib
from hamcrest import assert_that, empty
from mock import MagicMock, DEFAULT, patch
from nose.tools import eq_, ok_

from icm import vimsupport
from icm.tests import YouCompleteMeInstance
from ycmd.utils import ToBytes


def GetVariableValue_CompleteItemIs( word, abbr = None, menu = None,
                                     info = None, kind = None ):
  def Result( variable ):
    if variable == 'v:completed_item':
      return {
        'word': ToBytes( word ),
        'abbr': ToBytes( abbr ),
        'menu': ToBytes( menu ),
        'info': ToBytes( info ),
        'kind': ToBytes( kind ),
      }
    return DEFAULT
  return MagicMock( side_effect = Result )


def BuildCompletion( namespace = None, insertion_text = 'Test',
                     menu_text = None, extra_menu_info = None,
                     detailed_info = None, kind = None ):
  return {
    'extra_data': { 'required_namespace_import': namespace },
    'insertion_text': insertion_text,
    'menu_text': menu_text,
    'extra_menu_info': extra_menu_info,
    'kind': kind,
    'detailed_info': detailed_info,
  }


@contextlib.contextmanager
def _SetupForCsharpCompletionDone( ycm, completions ):
  with patch( 'icm.vimsupport.InsertNamespace' ):
    with patch( 'icm.vimsupport.TextBeforeCursor', return_value = '   Test' ):
      request = MagicMock()
      request.Done = MagicMock( return_value = True )
      request.RawResponse = MagicMock( return_value = completions )
      ycm._latest_completion_request = request
      yield


@patch( 'icm.vimsupport.CurrentFiletypes', return_value = [ 'cs' ] )
@YouCompleteMeInstance()
def GetCompleteDoneHooks_ResultOnCsharp_test( ycm, *args ):
  result = ycm.GetCompleteDoneHooks()
  eq_( 1, len( list( result ) ) )


@patch( 'icm.vimsupport.CurrentFiletypes', return_value = [ 'txt' ] )
@YouCompleteMeInstance()
def GetCompleteDoneHooks_EmptyOnOtherFiletype_test( ycm, *args ):
  result = ycm.GetCompleteDoneHooks()
  eq_( 0, len( list( result ) ) )


@patch( 'icm.vimsupport.CurrentFiletypes', return_value = [ 'txt' ] )
@YouCompleteMeInstance()
def OnCompleteDone_WithActionCallsIt_test( ycm, *args ):
  action = MagicMock()
  ycm._complete_done_hooks[ 'txt' ] = action
  ycm.OnCompleteDone()
  ok_( action.called )


@patch( 'icm.vimsupport.CurrentFiletypes', return_value = [ 'txt' ] )
@YouCompleteMeInstance()
def OnCompleteDone_NoActionNoError_test( ycm, *args ):
  ycm.OnCompleteDone()


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'Test' ) )
@YouCompleteMeInstance()
def FilterToCompletedCompletions_MatchIsReturned_test( ycm, *args ):
  completions = [ BuildCompletion( insertion_text = 'Test' ) ]
  result = ycm._FilterToMatchingCompletions( completions, False )
  eq_( list( result ), completions )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'A' ) )
@YouCompleteMeInstance()
def FilterToCompletedCompletions_ShortTextDoesntRaise_test( ycm, *args ):
  completions = [ BuildCompletion( insertion_text = 'AAA' ) ]
  ycm._FilterToMatchingCompletions( completions, False )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'Test' ) )
@YouCompleteMeInstance()
def FilterToCompletedCompletions_ExactMatchIsReturned_test( ycm, *args ):
  completions = [ BuildCompletion( insertion_text = 'Test' ) ]
  result = ycm._FilterToMatchingCompletions( completions, False )
  eq_( list( result ), completions )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( '   Quote' ) )
@YouCompleteMeInstance()
def FilterToCompletedCompletions_NonMatchIsntReturned_test( ycm, *args ):
  completions = [ BuildCompletion( insertion_text = 'A' ) ]
  result = ycm._FilterToMatchingCompletions( completions, False )
  assert_that( list( result ), empty() )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( '†es†' ) )
@YouCompleteMeInstance()
def FilterToCompletedCompletions_Unicode_test( ycm, *args ):
  completions = [ BuildCompletion( insertion_text = '†es†' ) ]
  result = ycm._FilterToMatchingCompletions( completions, False )
  eq_( list( result ), completions )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'Te' ) )
@patch( 'icm.vimsupport.TextBeforeCursor', return_value = '   Quote' )
@YouCompleteMeInstance()
def HasCompletionsThatCouldBeCompletedWithMoreText_MatchIsReturned_test(
    ycm, *args ):
  completions = [ BuildCompletion( insertion_text = 'Test' ) ]
  result = ycm._HasCompletionsThatCouldBeCompletedWithMoreText( completions )
  eq_( result, True )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'X' ) )
@patch( 'icm.vimsupport.TextBeforeCursor', return_value = '   Quote' )
@YouCompleteMeInstance()
def HasCompletionsThatCouldBeCompletedWithMoreText_ShortTextDoesntRaise_test(
    ycm, *args ):
  completions = [ BuildCompletion( insertion_text = 'AAA' ) ]
  ycm._HasCompletionsThatCouldBeCompletedWithMoreText( completions )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'Test' ) )
@patch( 'icm.vimsupport.TextBeforeCursor', return_value = '   Quote' )
@YouCompleteMeInstance()
def HasCompletionsThatCouldBeCompletedWithMoreText_ExactMatchIsntReturned_test(
    ycm, *args ):
  completions = [ BuildCompletion( insertion_text = 'Test' ) ]
  result = ycm._HasCompletionsThatCouldBeCompletedWithMoreText( completions )
  eq_( result, False )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( '   Quote' ) )
@patch( 'icm.vimsupport.TextBeforeCursor', return_value = '   Quote' )
@YouCompleteMeInstance()
def HasCompletionsThatCouldBeCompletedWithMoreText_NonMatchIsntReturned_test(
    ycm, *args ):
  completions = [ BuildCompletion( insertion_text = "A" ) ]
  result = ycm._HasCompletionsThatCouldBeCompletedWithMoreText( completions )
  eq_( result, False )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'Uniç' ) )
@patch( 'icm.vimsupport.TextBeforeCursor', return_value = 'Uniç' )
@YouCompleteMeInstance()
def HasCompletionsThatCouldBeCompletedWithMoreText_Unicode_test(
    ycm, *args ):
  completions = [ BuildCompletion( insertion_text = 'Uniçø∂¢' ) ]
  result = ycm._HasCompletionsThatCouldBeCompletedWithMoreText( completions )
  eq_( result, True )


@YouCompleteMeInstance()
def GetRequiredNamespaceImport_ReturnNoneForNoExtraData_test( ycm ):
  eq_( None, ycm._GetRequiredNamespaceImport( {} ) )


@YouCompleteMeInstance()
def GetRequiredNamespaceImport_ReturnNamespaceFromExtraData_test( ycm ):
  namespace = 'A_NAMESPACE'
  eq_( namespace, ycm._GetRequiredNamespaceImport(
    BuildCompletion( namespace )
  ) )


@YouCompleteMeInstance()
def GetCompletionsUserMayHaveCompleted_ReturnEmptyIfNotDone_test( ycm ):
  with _SetupForCsharpCompletionDone( ycm, [] ):
    ycm._latest_completion_request.Done = MagicMock( return_value = False )
    eq_( [], ycm.GetCompletionsUserMayHaveCompleted() )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'Te' ) )
@YouCompleteMeInstance()
def GetCompletionsUserMayHaveCompleted_ReturnEmptyIfPendingMatches_test(
    ycm, *args ):
  completions = [ BuildCompletion( None ) ]
  with _SetupForCsharpCompletionDone( ycm, completions ):
    eq_( [], ycm.GetCompletionsUserMayHaveCompleted() )


@YouCompleteMeInstance()
def GetCompletionsUserMayHaveCompleted_ReturnMatchIfExactMatches_test(
    ycm, *args ):
  info = [ 'NS', 'Test', 'Abbr', 'Menu', 'Info', 'Kind' ]
  completions = [ BuildCompletion( *info ) ]
  with _SetupForCsharpCompletionDone( ycm, completions ):
    with patch( 'icm.vimsupport.GetVariableValue',
                GetVariableValue_CompleteItemIs( *info[ 1: ] ) ):
      eq_( completions, ycm.GetCompletionsUserMayHaveCompleted() )


@YouCompleteMeInstance()
def GetCompletionsUserMayHaveCompleted_ReturnMatchIfExactMatchesEvenIfPartial_test( # noqa
    ycm, *args ):
  info = [ 'NS', 'Test', 'Abbr', 'Menu', 'Info', 'Kind' ]
  completions = [ BuildCompletion( *info ),
                  BuildCompletion( insertion_text = 'TestTest' ) ]
  with _SetupForCsharpCompletionDone( ycm, completions ):
    with patch( 'icm.vimsupport.GetVariableValue',
                GetVariableValue_CompleteItemIs( *info[ 1: ] ) ):
      eq_( [ completions[ 0 ] ], ycm.GetCompletionsUserMayHaveCompleted() )


@YouCompleteMeInstance()
def GetCompletionsUserMayHaveCompleted_DontReturnMatchIfNoExactMatchesAndPartial_test( # noqa
    ycm, *args ):
  info = [ 'NS', 'Test', 'Abbr', 'Menu', 'Info', 'Kind' ]
  completions = [ BuildCompletion( insertion_text = info[ 0 ] ),
                  BuildCompletion( insertion_text = 'TestTest' ) ]
  with _SetupForCsharpCompletionDone( ycm, completions ):
    with patch( 'icm.vimsupport.GetVariableValue',
                GetVariableValue_CompleteItemIs( *info[ 1: ] ) ):
      eq_( [], ycm.GetCompletionsUserMayHaveCompleted() )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'Test' ) )
@YouCompleteMeInstance()
def GetCompletionsUserMayHaveCompleted_ReturnMatchIfMatches_test( ycm, *args ):
  completions = [ BuildCompletion( None ) ]
  with _SetupForCsharpCompletionDone( ycm, completions ):
    eq_( completions, ycm.GetCompletionsUserMayHaveCompleted() )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'Test' ) )
@YouCompleteMeInstance()
def PostCompleteCsharp_EmptyDoesntInsertNamespace_test( ycm, *args ):
  with _SetupForCsharpCompletionDone( ycm, [] ):
    ycm._OnCompleteDone_Csharp()
    ok_( not vimsupport.InsertNamespace.called )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'Test' ) )
@YouCompleteMeInstance()
def PostCompleteCsharp_ExistingWithoutNamespaceDoesntInsertNamespace_test(
    ycm, *args ):
  completions = [ BuildCompletion( None ) ]
  with _SetupForCsharpCompletionDone( ycm, completions ):
    ycm._OnCompleteDone_Csharp()
    ok_( not vimsupport.InsertNamespace.called )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'Test' ) )
@YouCompleteMeInstance()
def PostCompleteCsharp_ValueDoesInsertNamespace_test( ycm, *args ):
  namespace = 'A_NAMESPACE'
  completions = [ BuildCompletion( namespace ) ]
  with _SetupForCsharpCompletionDone( ycm, completions ):
    ycm._OnCompleteDone_Csharp()
    vimsupport.InsertNamespace.assert_called_once_with( namespace )


@patch( 'icm.vimsupport.GetVariableValue',
        GetVariableValue_CompleteItemIs( 'Test' ) )
@patch( 'icm.vimsupport.PresentDialog', return_value = 1 )
@YouCompleteMeInstance()
def PostCompleteCsharp_InsertSecondNamespaceIfSelected_test( ycm, *args ):
  namespace = 'A_NAMESPACE'
  namespace2 = 'ANOTHER_NAMESPACE'
  completions = [
    BuildCompletion( namespace ),
    BuildCompletion( namespace2 ),
  ]
  with _SetupForCsharpCompletionDone( ycm, completions ):
    ycm._OnCompleteDone_Csharp()
    vimsupport.InsertNamespace.assert_called_once_with( namespace2 )
