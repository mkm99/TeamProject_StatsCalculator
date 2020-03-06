import unittest
from numpy.random import seed
from numpy.random import randint
import numpy as np
from statistics import mode
from scipy.stats import skew
from pprint import pprint

from StatisticsFunctions.mean import Mean
from StatisticsFunctions.median import Median
from StatisticsFunctions.meanDeviation import MeanDeviation
from StatisticsFunctions.mode import Mode
from StatisticsFunctions.quartiles import Quartile
from StatisticsFunctions.skewness import Skewness
from StatisticsFunctions.standardDeviation import StandardDeviation
from StatisticsFunctions.variance import Variance
from StatisticsFunctions.z_score import Z_score
from StatisticsFunctions.covariance import Covariance
from StatisticsFunctions.populationCorrelation import PopCorrelation
from StatisticsFunctions.sampleCorrelation import SampleCorrelation
from StatisticsFunctions.populationProportion import PopulationProportion
from RandomGenerator.N_numbers_from_list_seed import PickNumbersSeed
from RandomGenerator.pickSeed import PickSeed




class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 50, 15)
        self.testData2 = randint(1, 51, 15 )
        #pprint(self.testData)
        #pprint(self.testData2)

    def test_mean(self):
        mean = Mean.mean(self.testData)
        self.assertEqual(mean, 25.466666666666665)

    def test_mean2(self):
        result = np.mean(self.testData)
        self.assertEqual(result, 25.466666666666665)

    def test_median(self):
        median = Median.median(self.testData)
        self.assertEqual(median, 27.0)

    def test_median2(self):
        solution = np.median(self.testData)
        self.assertEqual(solution, 27.0)

    def test_standardDeviation(self):
        standardDeviation = StandardDeviation.standardDeviation(self.testData)
        self.assertEqual(standardDeviation, 14.01364414498321)

    def test_standardDeviation2(self):
        result = np.std(self.testData)
        self.assertEqual(result, 14.01364414498321)

    def test_variance(self):
        variance = Variance.variance(self.testData)
        self.assertEqual(variance, 196.3822222222222)

    def test_variance2(self):
        result = np.var(self.testData)
        self.assertEqual(result, 196.3822222222222)

    def test_mode(self):
        mode = Mode.mode(self.testData)
        self.assertEqual(mode, 16)

    def test_mode2(self):
        solution = mode(self.testData)
        self.assertEqual(solution,16)

    def test_meanDeviation(self):
        meanDeviation = MeanDeviation.meanDeviation(self.testData)
        self.assertEqual(meanDeviation, 12.835555555555555)

    def test_meanDeviation2(self):
        result = np.mean(np.absolute(self.testData - np.mean(self.testData)))
        self.assertEqual(result, 12.835555555555555)

    def test_quartiles(self):
        quartiles = Quartile.quartile(self.testData)
        self.assertEqual(quartiles, (13.0, 27.0, 37.0))

    def test_quartiles2(self):
        q1 = np.quantile(self.testData, .25)
        q2 = np.quantile(self.testData, .50)
        q3 = np.quantile(self.testData, .75)
        self.assertEqual((q1, q2, q3), (13.0, 27.0, 37.0))

    def test_skewness(self):
        skewness = Skewness.skewness(self.testData)
        self.assertEqual(skewness, 0.15182604770872699)

    def test_skewness2(self):
        result = skew(self.testData)
        self.assertEqual(result, 0.15182604770872699)

    def test_z_score(self):
        z_score = Z_score.z_score(2, self.testData)
        self.assertEqual(z_score, -1.3177633508895406)

    def test_zScore2(self):
        X = PickSeed.pickSeed(2, self.testData)
        mean = np.mean(self.testData)
        stdDev = np.std(self.testData)
        result = (X - mean) / stdDev
        self.assertEqual(result, -1.3177633508895406)

    def test_covariance(self):
        covariance = Covariance.covariance(self.testData, self.testData2)
        self.assertEqual(covariance, -19.961904761904755)

    def test_covariance2(self):
        result = np.cov(self.testData, self.testData2)[0,1]
        self.assertEqual(result, -19.961904761904755)

    def test_popCorrelation(self):
        result = PopCorrelation.correlation(self.testData, self.testData2)
        self.assertEqual(result, -0.09958703367427517)

    def test_popCorrelation2(self):
        cov = Covariance.covariance(self.testData, self.testData2)
        stdDevA = np.std(self.testData)
        stdDevB = np.std(self.testData2)
        result = cov/(stdDevA*stdDevB)
        self.assertEqual(result, -0.09958703367427517)

    def test_sampleCorrelation(self):
        result = SampleCorrelation.correlation(3, self.testData, self.testData2)
        self.assertEqual(result, -0.5940762068478092)

    def test_sampleCorrelation2(self):
        sampleDataA = PickNumbersSeed.pickNumbers(3, self.testData, 5)
        sampleDataB = PickNumbersSeed.pickNumbers(3, self.testData2, 5)

        cov = Covariance.covariance(sampleDataA, sampleDataB)
        stdDevA = np.std(sampleDataA)
        stdDevB = np.std(sampleDataB)
        result = cov / (stdDevA * stdDevB)
        self.assertEqual(result, -0.5940762068478092)

    def test_population_Proportion(self):
        result = PopulationProportion.proportion(3, self.testData, 4)
        self.assertEqual(result, 0.26666666666666666)

    def test_population_Proportion2(self):
        subData = PickNumbersSeed.pickNumbers(3, self.testData, 4)
        result = len(subData) / len(self.testData)
        self.assertEqual(result, 0.26666666666666666)


if __name__ == '__main__':
    unittest.main()


