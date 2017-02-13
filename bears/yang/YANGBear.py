from os.path import dirname

from coalib.bearlib.abstractions.Linter import linter
from dependency_management.requirements.PipRequirement import PipRequirement


@linter(executable='pyang',
        use_stderr=True,
        output_format='regex',
        output_regex=r'.*:(?P<line>\d+):\s*(?P<message>.*)')
class YANGBear:
    """
    Lints `YANG <https://en.wikipedia.org/wiki/YANG>`__ model files using
    ``pyang``.

    From `RFC 7950 <https://tools.ietf.org/html/rfc7950>`__:

    _"YANG is a data modeling language used to model configuration data,
    state data, Remote Procedure Calls, and notifications for network
    management protocols."_

    See <https://pypi.python.org/pypi/pyang> for more information.
    """
    LANGUAGES = {'YANG'}
    REQUIREMENTS = {PipRequirement('pyang', '1.7.1')}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Formatting', 'Syntax'}

    @staticmethod
    def create_arguments(filename, file, config_file):
        # -p defines the search path for other YANG modules imported by
        # the current file. At least the file's own directory should be
        # given here, since it's is not implicitly searched by pyang
        return '-p', dirname(filename), '--lint', filename
