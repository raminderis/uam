import pytest

from hr import cli

def test_parser_fails_without_arguments():
    """
    Without a path, the parser should exit with an error.
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_parser_succeeds_with_a_path():
    """
    With a path, the parser should not give an error
    """
    parser = cli.create_parser()
    args = parser.parse_args(['/some/path'])
    assert args.path == '/some/path'

def test_parser_export_flag():
    """
    the export value should default to False, but set to True when passed to the parser
    """
    parser = cli.create_parser()
    args = parser.parse_args(['/some/path'])
    assert args.export == False

    args = parser.parse_args(['--export','/some/path'])
    assert args.export == True
