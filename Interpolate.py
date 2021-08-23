"""For some known inputs and some known outputs,
this script will find the coefficients of the corresponding polynomial function."""

import numpy as np
import matplotlib.pyplot as plt


class PolyInterpolate:
    def __init__(self, Inputs=[0], Outputs=[0]):
        self.inputs = Inputs
        self.outputs = Outputs
        self.coeffs = np.array([])

    # Returns Vandermonde matrix of polynomial
    def find_vandermonde(self):
        return np.vander(self.inputs)

    # Inverts the Vandermonde matrix
    def invert_vandermonde(self):
        self.find_vandermonde()
        return np.linalg.inv(self.find_vandermonde())

    # Returns the coefficients of the polynomial by matrix multiplying the inverted vandermonde matrix by the vector of outputs
    def find_coefficients(self):
        self.invert_vandermonde()
        self.coeffs = np.matmul(self.invert_vandermonde(), self.outputs)
        self.coeffs = np.flipud(self.coeffs)
        return self.coeffs

    def __repr__(self):
        self.find_vandermonde()
        self.invert_vandermonde()
        self.find_coefficients()
        return f'{self.coeffs}'