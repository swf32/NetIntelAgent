"""
NetIntelAgent - Network Intelligence Agent
Core mathematical calculations for probability distributions
"""

import numpy as np

class MathEquations:
    
    
    def __init__(self, source_count, pj, P, Ks, Kf, Fs, Ff, Nmax):
        """Initialize the MathEquations class with source data
        
        Args:
            source_count: Number of sources
            pj: Probability of success for each source
            P: Transition probabilities
            Ks: Success step counts for each source
            Kf: Failure step counts for each source
            Fs: Success probability distributions
            Ff: Failure probability distributions
            Nmax: Time limit (maximum number of steps)
        """
        self.source_count = source_count
        self.pj = pj
        self.P = P
        self.Ks = Ks
        self.Kf = Kf
        self.Fs = Fs
        self.Ff = Ff
        self.Nmax = Nmax
        
        
        self.Findef = None
        self.Fand = None
        self.For = None
        self.Frepl = None
        self.Fnonrepl = None
        self.Fs_all = None
        self.Ff_all = None
        
        
        self.Kindef = None
        self.Kand = None
        self.Kor = None
        self.Krepl_ = None
        self.Ks_all = None
        self.Kf_all = None
        
        
        self.MO_indef = 0.0
        self.MO_and = 0.0
        self.MO_or = 0.0
        self.MO_replic = 0.0
        self.MO_nonreplic = 0.0
        self.MO_Fs_all = 0.0
        self.MO_Ff_all = 0.0
        
        
        self.PNmax_indef = 0.0
        self.PNmax_and = 0.0
        self.PNmax_or = 0.0
        self.PNmax_replic = 0.0
        self.PNmax_nonreplic = 0.0
        self.PNmax_Fs_all = 0.0
        self.PNmax_Ff_all = 0.0
        
        
        self.Fjs = [{} for _ in range(source_count)]
        self.Fjf = [{} for _ in range(source_count)]
        self.Fj = [{} for _ in range(source_count)]
        self.Kj = self._kj_init()
        self._fj_sf_init()
        self._fj_init()
        
        
        self.Krepl = None
    
    def _kj_init(self):
        
        Kj = []
        for i in range(self.source_count):
            
            combined = sorted(set(self.Ks[i] + self.Kf[i]))
            Kj.append(combined)
        return Kj
    
    def _fj_sf_init(self):
        
        for i in range(self.source_count):
            
            for j, k in enumerate(self.Ks[i]):
                self.Fjs[i][k] = self.Fs[i][j]
            
            
            for j, k in enumerate(self.Kf[i]):
                self.Fjf[i][k] = self.Ff[i][j]
    
    def _fj_init(self):
        
        for i in range(self.source_count):
            for k in self.Kj[i]:
                
                s_prob = self.Fjs[i].get(k, 0.0)
                f_prob = self.Fjf[i].get(k, 0.0)
                
                
                self.Fj[i][k] = self.pj[i] * s_prob + (1.0 - self.pj[i]) * f_prob
    
    def _kindef_define(self):
        
        all_steps = []
        for i in range(self.source_count):
            all_steps.extend(self.Ks[i])
        
        self.Kindef = sorted(set(all_steps))
    
    def indefinit_func(self):
        
        if self.Kindef is None:
            self._kindef_define()
        
        self.Findef = [0.0] * len(self.Kindef)
        
        
        for i, k in enumerate(self.Kindef):
            for j in range(self.source_count):
                if k in self.Fj[j]:
                    self.Findef[i] += self.Fj[j][k] * self.P[j]
        
        
        self.PNmax_indef = sum(self.Findef[:min(self.Nmax, len(self.Findef))])
        
        
        self.MO_indef = sum(p * k for p, k in zip(self.Findef, self.Kindef))
    
    def _kand(self):
        
        max_values = [max(self.Kj[i]) for i in range(self.source_count)]
        min_values = [min(self.Kj[i]) for i in range(self.source_count)]
        
        
        start = max(min_values)
        
        end = max(max_values)
        
        
        all_k = []
        for i in range(self.source_count):
            all_k.extend(self.Kj[i])
        
        
        self.Kand = sorted(set(k for k in all_k if k >= start))
    
    def _kor(self):
        
        max_values = [max(self.Kj[i]) for i in range(self.source_count)]
        min_values = [min(self.Kj[i]) for i in range(self.source_count)]
        
        
        start = min(min_values)
        
        end = min(max_values)
        
        
        all_k = []
        for i in range(self.source_count):
            all_k.extend(self.Kj[i])
        
        
        self.Kor = sorted(set(k for k in all_k if start <= k <= end))
    
    def _summa(self, F, K, max_val, ctrl=False):
        """Calculate the sum of probabilities for steps less than (or equal to) max_val
        
        Args:
            F: Dictionary of step-probability pairs
            K: Array of step values
            max_val: Maximum step value to consider
            ctrl: If True, include steps equal to max_val
        
        Returns:
            Sum of probabilities
        """
        if ctrl:
            return sum(F.get(k, 0.0) for k in K if k <= max_val)
        else:
            return sum(F.get(k, 0.0) for k in K if k < max_val)
    
    def fand(self):
        
        if self.Kand is None:
            self._kand()
        
        self.Fand = [0.0] * len(self.Kand)
        
        
        for i, k in enumerate(self.Kand):
            for j in range(self.source_count):
                if k in self.Fj[j]:
                    
                    product = self.Fj[j][k]
                    
                    
                    for m in range(self.source_count):
                        if m == j:
                            continue
                        
                        if m >= j:
                            product *= self._summa(self.Fj[m], self.Kj[m], k, True)
                        else:
                            product *= self._summa(self.Fj[m], self.Kj[m], k, False)
                    
                    self.Fand[i] += product
        
        
        self.PNmax_and = sum(self.Fand[:min(self.Nmax, len(self.Fand))])
        
        
        self.MO_and = sum(p * k for p, k in zip(self.Fand, self.Kand))
    
    def for_calculation(self):
        
        if self.Kor is None:
            self._kor()
        
        self.For = [0.0] * len(self.Kor)
        
        
        for i, k in enumerate(self.Kor):
            for j in range(self.source_count):
                if k in self.Fj[j]:
                    
                    product = self.Fj[j][k]
                    
                    
                    for m in range(self.source_count):
                        if m == j:
                            continue
                        
                        if m >= j:
                            product *= (1.0 - self._summa(self.Fj[m], self.Kj[m], k, True))
                        else:
                            product *= (1.0 - self._summa(self.Fj[m], self.Kj[m], k, False))
                    
                    self.For[i] += product
        
        
        self.PNmax_or = sum(self.For[:min(self.Nmax, len(self.For))])
        
        
        self.MO_or = sum(p * k for p, k in zip(self.For, self.Kor))
    
    def _krepl(self):
        
        self.Krepl = [None] * self.source_count
        self.Krepl[0] = self.Kj[0][:]
        
        for i in range(1, self.source_count):
            
            possible_steps = []
            
            
            
            prev_steps = self.Krepl[i-1]
            
            for prev_step in prev_steps:
                for curr_step in self.Kj[i]:
                    possible_steps.append(prev_step + curr_step)
            
            self.Krepl[i] = sorted(set(possible_steps))
        
        
        all_steps = []
        for steps in self.Krepl:
            all_steps.extend(steps)
        
        self.Krepl_ = sorted(set(all_steps))
    
    def _prepl(self, f, k, nmax=None):
        """Calculate the probability of completion within nmax steps
        
        Args:
            f: Dictionary of step-probability pairs
            k: Array of step values
            nmax: Maximum number of steps to consider (defaults to self.Nmax)
        
        Returns:
            Probability of completion
        """
        if nmax is None:
            nmax = self.Nmax
            
        return sum(f.get(step, 0.0) for step in k if step <= nmax)
    
    def _pprepl(self, f, k, count):
        """Calculate the product of complements of completion probabilities
        
        Args:
            f: Array of dictionaries with step-probability pairs
            k: Array of arrays with step values
            count: Number of sources to consider
            
        Returns:
            Product of complements of completion probabilities
        """
        product = 1.0
        for i in range(count):
            product *= (1.0 - self._prepl(f[i], k[i]))
        return product
    
    def _ppnonrepl(self, f, k, count):
        """Calculate the product of completion probabilities
        
        Args:
            f: Array of dictionaries with step-probability pairs
            k: Array of arrays with step values
            count: Number of sources to consider
            
        Returns:
            Product of completion probabilities
        """
        product = 1.0
        for i in range(count):
            product *= self._prepl(f[i], k[i])
        return product
    
    def frepl(self):
        
        if self.Krepl is None:
            self._krepl()
        
        
        array = [{} for _ in range(self.source_count)]
        
        
        for k in self.Krepl[0]:
            array[0][k] = self.Fj[0].get(k, 0.0)
        
        
        for j in range(1, self.source_count):
            for k in self.Krepl[j]:
                prob_sum = 0.0
                
                for prev_k in self.Krepl[j-1]:
                    step_diff = k - prev_k
                    if step_diff in self.Fj[j]:
                        prob_sum += array[j-1][prev_k] * self.Fj[j][step_diff]
                
                array[j][k] = prob_sum
        
        
        self.Frepl = [0.0] * len(self.Krepl_)
        
        for i, k in enumerate(self.Krepl_):
            prob_sum = 0.0
            
            for m in range(self.source_count):
                if m + 1 != self.source_count:
                    if k in array[m]:
                        p_complete = self._prepl(array[m], self.Krepl[m])
                        p_others = self._pprepl(array, self.Krepl, m)
                        prob_sum += p_complete * array[m][k] * p_others
                else:
                    if k in array[m]:
                        p_others = self._pprepl(array, self.Krepl, m)
                        prob_sum += array[m][k] * p_others
            
            self.Frepl[i] = prob_sum
        
        
        self.PNmax_replic = sum(self.Frepl[:min(self.Nmax, len(self.Frepl))])
        
        
        self.MO_replic = sum(p * k for p, k in zip(self.Frepl, self.Krepl_))
    
    def fnonrepl(self):
        
        if self.Krepl is None:
            self._krepl()
        
        
        array = [{} for _ in range(self.source_count)]
        
        
        for k in self.Krepl[0]:
            array[0][k] = self.Fj[0].get(k, 0.0)
        
        
        for j in range(1, self.source_count):
            for k in self.Krepl[j]:
                prob_sum = 0.0
                
                for prev_k in self.Krepl[j-1]:
                    step_diff = k - prev_k
                    if step_diff in self.Fj[j]:
                        prob_sum += array[j-1][prev_k] * self.Fj[j][step_diff]
                
                array[j][k] = prob_sum
        
        
        self.Fnonrepl = [0.0] * len(self.Krepl_)
        
        for i, k in enumerate(self.Krepl_):
            prob_sum = 0.0
            
            for m in range(self.source_count):
                if m + 1 != self.source_count:
                    if k in array[m]:
                        p_incomplete = 1.0 - self._prepl(array[m], self.Krepl[m])
                        p_others = self._ppnonrepl(array, self.Krepl, m)
                        prob_sum += p_incomplete * array[m][k] * p_others
                else:
                    if k in array[m]:
                        p_others = self._ppnonrepl(array, self.Krepl, m)
                        prob_sum += array[m][k] * p_others
            
            self.Fnonrepl[i] = prob_sum
        
        
        self.PNmax_nonreplic = sum(self.Fnonrepl[:min(self.Nmax, len(self.Fnonrepl))])
        
        
        self.MO_nonreplic = sum(p * k for p, k in zip(self.Fnonrepl, self.Krepl_))
    
    def _ksf_all(self):
        
        
        all_s_steps = []
        for i in range(self.source_count):
            all_s_steps.extend(self.Ks[i])
        self.Ks_all = sorted(set(all_s_steps))
        
        
        all_f_steps = []
        for i in range(self.source_count):
            all_f_steps.extend(self.Kf[i])
        self.Kf_all = sorted(set(all_f_steps))
    
    def fsf_all(self):
        
        self._ksf_all()
        
        
        self.Fs_all = [0.0] * len(self.Ks_all)
        self.Ff_all = [0.0] * len(self.Kf_all)
        
        
        for i, k in enumerate(self.Ks_all):
            for j in range(self.source_count):
                if k in self.Fjs[j]:
                    self.Fs_all[i] += self.P[j] * self.pj[j] * self.Fjs[j][k]
        
        
        for i, k in enumerate(self.Kf_all):
            for j in range(self.source_count):
                if k in self.Fjf[j]:
                    self.Ff_all[i] += self.P[j] * (1.0 - self.pj[j]) * self.Fjf[j][k]
        
        
        self.PNmax_Fs_all = sum(self.Fs_all[:min(self.Nmax, len(self.Fs_all))])
        self.PNmax_Ff_all = sum(self.Ff_all[:min(self.Nmax, len(self.Ff_all))])
        
        
        self.MO_Fs_all = sum(p * k for p, k in zip(self.Fs_all, self.Ks_all))
        self.MO_Ff_all = sum(p * k for p, k in zip(self.Ff_all, self.Kf_all))