# This code is part of Qiskit.
#
# (C) Copyright IBM 2021, 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
A class that formats documentation sections.
"""
from typing import List
from .utils import _check_no_indent, _write_options


class DocstringSectionFormatter:
    """A class that formats parsed docstring lines.

    This formatter formats sections with Google Style Python Docstrings with
    several reStructuredText directives.
    """

    def __init__(self, indent: str):
        self.indent = indent

    def format_header(self, lines: List[str]) -> List[str]:
        """Format header section."""
        format_lines = lines
        format_lines.append("")

        return format_lines

    @_check_no_indent
    def format_overview(self, lines: List[str]) -> List[str]:
        """Format overview section."""
        return [".. rubric:: Overview", "", *lines, ""]

    @_check_no_indent
    def format_reference(self, lines: List[str]) -> List[str]:
        """Format reference section."""
        return [".. rubric:: References", "", *lines, ""]

    def format_warning(self, lines: List[str]) -> List[str]:
        """Format warning section."""
        format_lines = [".. warning::", ""]
        format_lines.extend(self.indent + line for line in lines)
        format_lines.append("")

        return format_lines

    @_check_no_indent
    def format_example(self, lines: List[str]) -> List[str]:
        """Format example section."""
        return [".. rubric:: Example", "", *lines, ""]

    def format_note(self, lines: List[str]) -> List[str]:
        """Format notification section."""
        format_lines = [".. note::", ""]
        format_lines.extend(self.indent + line for line in lines)
        format_lines.append("")

        return format_lines

    @_check_no_indent
    def format_see_also(self, lines: List[str]) -> List[str]:
        """Format see also section."""
        return [".. rubric:: See also", "", *lines, ""]

    @_check_no_indent
    def format_manual(self, lines: List[str]) -> List[str]:
        """Format user manual section."""
        return [".. rubric:: User manual", "", *lines, ""]

    @_check_no_indent
    def format_init(self, lines: List[str]) -> List[str]:
        """Format user manual section."""
        return [".. rubric:: Initialization", "", *lines, ""]


class ExperimentSectionFormatter(DocstringSectionFormatter):
    """Formatter for experiment class."""

    @_check_no_indent
    def format_analysis_ref(self, lines: List[str]) -> List[str]:
        """Format analysis class reference section."""
        return [".. rubric:: Analysis class reference", "", *lines, ""]

    @_check_no_indent
    def format_experiment_opts(self, lines: List[str]) -> List[str]:
        """Format experiment options section."""
        format_lines = [
            ".. rubric:: Experiment options",
            "",
            "These options can be set by the :meth:`set_experiment_options` method.",
            "",
        ]
        format_lines.extend(iter(_write_options(lines, self.indent)))
        format_lines.append("")

        return format_lines


class AnalysisSectionFormatter(DocstringSectionFormatter):
    """Formatter for analysis class."""

    @_check_no_indent
    def format_analysis_opts(self, lines: List[str]) -> List[str]:
        """Format analysis options section."""
        format_lines = [
            ".. rubric:: Analysis options",
            "",
            "These are the keyword arguments of :meth:`run` method.",
            "",
        ]
        format_lines.extend(iter(_write_options(lines, self.indent)))
        format_lines.append("")

        return format_lines

    @_check_no_indent
    def format_fit_model(self, lines: List[str]) -> List[str]:
        """Format fit model section."""
        return [
            ".. rubric:: Fit model",
            "",
            "This is the curve fitting analysis. ",
            "The following equation(s) are used to represent curve(s).",
            "",
            *lines,
            "",
        ]

    @_check_no_indent
    def format_fit_parameters(self, lines: List[str]) -> List[str]:
        """Format fit parameter section."""
        return [
            ".. rubric:: Fit parameters",
            "",
            "The following fit parameters are estimated during the analysis.",
            "",
            *lines,
            "",
        ]


class VisualizationSectionFormatter(DocstringSectionFormatter):
    """Formatter for visualization classes."""

    @_check_no_indent
    def format_opts(self, lines: List[str]) -> List[str]:
        """Format options section."""

        format_lines = [
            ".. rubric:: Options",
            "",
            "The following can be set using :meth:`set_options`.",
            "",
        ]
        format_lines.extend(iter(_write_options(lines, self.indent)))
        format_lines.append("")

        return format_lines

    @_check_no_indent
    def format_figure_opts(self, lines: List[str]) -> List[str]:
        """Format figure options section."""
        format_lines = [
            ".. rubric:: Figure options",
            "",
            "The following can be set using :meth:`set_figure_options`.",
            "",
        ]
        format_lines.extend(iter(_write_options(lines, self.indent)))
        format_lines.append("")

        return format_lines
