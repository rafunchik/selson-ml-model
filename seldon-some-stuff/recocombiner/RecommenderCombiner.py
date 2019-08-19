import logging
logger = logging.getLogger(__name__)

class RecommenderCombiner(object):
    def __init__(self, metrics_ok=True):
        print("Reco Combiner Init called")

    def aggregate(self, Xs, features_names):
        print("Reco Combiner aggregate called")
        logger.info(Xs)
        try:
          a = Xs[0]
        except:
          a = None
        return a or Xs[1]

