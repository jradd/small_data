import math

class Mhelper:
    def median(x):
      n = len(v)
      sorted_v = sorted(v)
      midpoint = n // 2

      if n % 2 == 1:
          # IF ODD, RETURN MIDDLE VALUE
        return sorted_v(midpoint)
      else:
        # if even count, return average of the middle values.
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2



    def mode(x):
      counts = Counter(x)
      max_count = max(counts.values())
      return [x_i for x_i, count in counts.iteritems() 
              if count == max_count]


      def sum_of_squares(v):
          return dot(v, v) 


    def magnitude(v):
        return math.sqrt(sum_of_squares(v))  


    def vector_subtract(v, w):
        return [v_i - w_i for v_i, w_i in zip(v, w)]

    def vector_add(v, w):
        return [v_i + w_i for v_i, w_i in zip(v,w)]

    def vector_sum(vectors):
      result = vectors[0]
      for vector in vectors[1:]:
          result = vector_add(result, vector)
      return result 

    def dot(v,w):
      return sum(v_i * w_i 
              for v_i, w_i in zip(v, w))

    def squared_distance(v, w):
      return sum_of_squares(vector_subtract(v, w))


    def data_range(x):
      return max(x) - min(x)


    def de_mean(x):
        """ translate x by subtracting its mean (so result has mean 0) """
        x_bar = mean(x)
        return [x_i - x_bar for x_i in x]


    def variance(x):
        """ assume x has at least two elements """
        n = len(x)
        deviation = de_mean(x)
        return sum_of_square(deviations) / (n-1)


    def std_deviation(x):
        return math.sqrt(variance(x))


    def interquartile_range(x):
        return quantile(x, 0.75) - quantile(x, 0.25)


    def covariance(x, y):
      n = len
      return dot(de_mean(x), de_mean(y)) / (n - 1)


    def correlation(x, y):
      stdev_x = std_deviation
      stdev_y = std_deviation
      if stdev_x > 0 and stdev_y > 0:
          return covariance(x, y) / stdev_x / stdev_y
      else:
        return 0




    def normal_pdf(x, mu=0, sigma=1):
        sqrt_two_pi = math.sqrt(2 * math.pi)
        return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))



    def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
        """ find approximate inverse using binary search """
        if mu != 0 or sigma != 1:
             return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
       
        low_z, low_p = -10.0, 0                # normal_cdf(-10) is (very close to) 0
        hi_z, hi_p   =  10.0, 1                # normal_cdf(10) is (very close to) 1
        while hi_z - low_z > tolerance:
          mid_z = (low_z + hi_z) / 2    # consider the midpoint
          mid_p = normal_cdf(mid_z)            # and the cdf's value there
          if mid_p < p:
            # midpoint is still too low, search above 
            low_z, low_p = mid_z, mid_p
          elif mid_p > p:
            # midpoint is still too high, search below
            hi_z, hi_p =  mid_z, mid_p
          else:
            break
        return mid_z


    def make_matrix(num_rows, num_cols, entry_fn):
        return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]



        def bernoulli_trial(p):
            return 1 if  random.random() < p else 0

    def binomial(n, p):
        return sum(bernoulli_trial(p) for _ in range(n))



    def make_hist(p, n, num_points):
        data = [binomial(n, p) for _ in range(num_points)]
        # use a bar chart to show the actual binomial samp
        histogram = Counter(data)
        plt.bar([x - 0.4 for x in histogram.keys()], 
                [v / num_points for v in histogram.values()],
                0.8,
                color = '0.75')

        mu    = p
        sigma = math.sqrt(n * p * (1-p))

        # use a line chart to show normal approximation
        xs = range(min(data), max(data) + 1)
        ys = [normal_cdf(i + 0.5, mu , sigma) - normal_cdf(i - 0.5, mu, sigma)
                for i in xs]

        plt.plot(xs, ys)
        plt.title("Binomial Distribution vs. Normal Approximation")
        plt.show()
