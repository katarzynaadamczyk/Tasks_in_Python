'''

my solution to task: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        act_min, profit = prices[0], 0
        for val in prices[1:]:
            if val < act_min:
                act_min = val
            elif profit < val - act_min:
                profit = val - act_min
        return profit
        
        

def main():
    sol = Solution()
    
    # test 1
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices), 'should equal 5')
    
    # test 2
    prices = [7,6,4,3,1]
    print(sol.maxProfit(prices), 'should equal 0')
    
    # test 3
    prices = [414,863,393,674,205,793,229,379,37,455,594,36,312,667,441,411,514,344,681,359,865,124,984,670,509,337,495,266,275,356,26,229,51,557,292,975,551,985,445,710,467,31,\
890,694,127,349,631,322,595,59,433,173,944,305,662,379,864,835,355,411,506,10,716,918,872,716,887,453,706,416,245,611,6,403,894,94,852,733,890,131,481,723,571,335,\
695,475,112,245,389,754,439,990,771,282,935,746,422,627,570,101,212,248,123,633,842,110,272,352,910,926,726,502,396,49,444,581,504,145,765,710,785,126,232,386,245,\
613,43,591,638,179,438,838,5,486,170,960,273,347,8,176,884,569,528,442,839,573,953,102,802,659,51,675,110,76,531,783,539,806,363,333,214,919,473,303,690,917,793,2,\
504,7,584,734,527,561,484,648,622,123,655,977,235,999,714,963,921,801,237,752,127,484,772,483,62,544,938,845,218,32,832,174,561,635,44,903,972,550,291,12,234,24,\
750,182,257,265,276,926,409,865,170,587,35,813,628,991,829,573,226,69,979,188,285,582,276,951,114,634,797,720,306,365,862,416,8,174,446,555,132,578,152,582,214,673,\
156,899,613,871,789,378,434,464,532,356,884,83,744,126,773,537,149,723,653,967,574,87,463,312,416,3,667,339,471,237,540,860,709,867,474,769,344,52,633,784,199,239,\
735,362,131,14,376,683,532,154,618,505,773,970,207,208,926,192,273,338,282,874,679,932,67,593,412,932,807,456,637,360,988,839,345,890,409,316,535,123,234,480,368,\
515,98,486,343,79,989,768,443,943,628,184,452,379,557,265,904,327,353,698,158,148,133,972,179,934,90,976,199,187,142,126,55,764,64,593,310,284,307,43,855,51,382,483,\
251,601,675,723,467,501,217,896,433,759,156,979,954,802,308,591,637,920,867,411,82,433,320,548,571,254,771,597,761,93,106,163,662,500,764,587,801,876,338,431,771,\
824,219,446,344,311,532,833,921,616,536,645,292,256,764,560,885,434,640,97,926,150,755,562,636,768,713,710,256,64,293,390,223,509,614,457,182,881,646,743,700,995,\
94,801,173,579,104,107,557,736,292,483,66,767,781,151,592,169,482,775,608,398,399,38,548,185,720,226,832,54,463,57,36,97,416,611,663,357,586,286,744,535,671,202,\
26,443,613,739,213,672,409,534,62,697,985,920,809,473,48,895,920,871,527,121,339,195,511,80,940,647,530,418,344,139,53,593,638,961,183,392,208,312,522,448,844,182,\
358,589,152,575,600,715,33,457,865,20,565,508,101,670,407,123,154,977,498,495,736,791,883,896,793,923,409,370,524,748,926,682,800,481,858,388,475,847,775,326,707,\
792,22,807,60,65,118,10,323,410,326,340,803,386,557,633,188,309,589,981,616,71,516,950,313,781,458,488,314,535,114,197,53,626,541,38,537,770,311,444,797,703,216,\
944,879,42,863,239,350,469,207,709,79,319,254,514,626,675,877,117,490,870,709,779,974,240,176,461,478,278,800,561,526,663,221,989,498,848,128,367,606,554,945,54,\
968,314,244,437,388,584,490,977,282,316,598,106,883,275,426,335,969,809,697,595,814,237,379,136,585,742,516,492,476,646,372,423,857,1,763,733,437,420,720,181,149,\
439,125,512,910,621,890,422,84,622,680,736,686,941,786,288,179,152,900,773,295,602,319,979,933,533,574,559,392,413,122,383,410,754,735,793,622,152,403,429,397,315,\
905,186,209,408,212,711,996,315,706,835,8,887,235,406,314,5,942,894,440,371,398,257,233,628,807,901,370,287,62,799,261,635,991,417,746,442,153,676,566,231,716,927,\
458,489,113,757,592,170,540,717,441,697,887,403,988,468,132,809,705,480,335,744,317,742,139,861,20,161,693,474,342,939,683,796,49,263,62,225,968,624,223,724,55,964,\
821,242,916,149,733,872,24,442,360,252,693,813,567,672,181,173,76,646,286,660,50,613,445,296,821,30,729,632,491,849,954,188,216,257,104,168,275,650,707,448,513,463,\
908,198,272,655,258,758,793,204,45,352,488,791,361,963,626,980,337,594,259,215,338,670,332,211,430,406,875,839,474,878,181,890,753,923,160,872,227,348,123,48,677,365,\
56,901,179,41,822,724,188,184,746,617,84,714,575,94,242,980,665,336,175,67,676,51,498,787,861,414,329,979,596,743,685,546,19,906,536,747,618,41,106,632,709,922,495,947,\
720,254,95,422,292,758,73,58,880,393,330,783,732,103,400,592,970,245,34,83,468,935,805,514,113,404,26,237,995,143,269,737,213,595,770,405,203,64,904,501,132,347,983,418,\
974,242,883,945,597,88,245,612,352,714,419,983,157,627,688,950,469,59,510,921,422,438,495,907,452,501,394,79,45,186,359,97,181,830,542,428,520,801,275,137,753,665,403,\
116,653,299,500,851,913,801,659,483,23,188,550,605,728,985,962,521,946,351,741,559,217,487,411,863,140,257,540,689,603,117,328,997,149,171,456,233,474,709,903,563,525,\
771,656,692,556,744,331,742,947,758,663,648,604,347,417,477,524,788,231,771,40,406,830,758,307,747,583,985,102,681,76,331,822,938,307,457,631,442,584,830,494,707,775,\
528,483,112,226,585,779,986,28,246,448,833,550,629,460,334,6,149,236,191,523,259,697,958,288,634,512,314,788,30,376,313,305,706,882,222,703,946,555,233,69,189,498,237,\
180,663,19,717,998,881,615,47,512,826,488,631,504,542,264,182,771,633,355,493,223,330,113,417,756,588,712,359,265,842,701,757,835,959,254,983,914,462,356,602,876,513,\
972,19,566,635,884,446,115,91,545,878,381,262,75,975,674,491,138,360,69,236,207,935,911,770,747,151,686,322,972,315,834,984,186,793,942,942,907,849,956,79,546,226,176,\
164,687,776,546,863,661,397,735,221,495,984,45,458,218,834,239,857,81,599,482,481,21,471,175,925,719,607,724,365,621,64,644,200,718,574,954,528,285,683,898,665,266,315,\
416,318,325,306,75,988,907,913,619,1,447,366,412,451,797,540,748,290,401,996,312,832,26,885,491,685,555,512,829,999,743,376,835,824,207,341,609,408,597,275,741,225,967,\
331,839,243,696,337,71,610,200,455,572,115,800,707,172,79,211,721,844,360,306,874,498,831,623,693,684,898,0,271,732,678,487,367,639,574,327,276,887,165,580,460,292,837]
    print(sol.maxProfit(prices))

if __name__ == '__main__':
    main()