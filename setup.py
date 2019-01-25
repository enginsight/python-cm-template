    #
#   # #   Enginsight GmbH
# # # #   Geschäftsführer: Mario Jandeck, Eric Range
# #   #   Hans-Knöll-Straße 6, 07745 Jena
  #   

import random

one_metric = random.randint(1,101)
another_metric = random.randint(1,101)

print("""

__METRICS__={
  "one_metric": %d,
  "another_metric": %d
}

""" % (one_metric, another_metric))
