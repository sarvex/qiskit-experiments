# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""A FakeExperiment for testing."""

import numpy as np
from matplotlib.figure import Figure as MatplotlibFigure
from qiskit_experiments.framework import BaseExperiment, BaseAnalysis, Options, AnalysisResultData


class FakeAnalysis(BaseAnalysis):
    """
    Dummy analysis class for test purposes only.
    """

    def __init__(self, **kwargs):
        super().__init__()
        self._kwargs = kwargs

    def _run_analysis(self, experiment_data):
        seed = self.options.get("seed", None)
        rng = np.random.default_rng(seed=seed)
        analysis_results = [
            AnalysisResultData(f"result_{i}", value) for i, value in enumerate(rng.random(3))
        ]
        figures = None
        if add_figures := self.options.get("add_figures", False):
            figures = [MatplotlibFigure()]
        return analysis_results, figures


class FakeExperiment(BaseExperiment):
    """Fake experiment class for testing."""

    @classmethod
    def _default_experiment_options(cls) -> Options:
        options = super()._default_experiment_options()
        options.dummyoption = None
        return options

    def __init__(self, physical_qubits=None):
        """Initialise the fake experiment."""
        if physical_qubits is None:
            physical_qubits = [0]
        super().__init__(physical_qubits, analysis=FakeAnalysis())

    def circuits(self):
        """Fake circuits."""
        return []
