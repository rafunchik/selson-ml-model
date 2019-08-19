import joblib
import spotlight
# import torch
import logging
# import sys


class MyModel(object):
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """

    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """
        logging.info("Initializing")
        # import pkg_resources
        # installed_packages = pkg_resources.working_set
        # installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
        #                                   for i in installed_packages])
        # logging.error(installed_packages_list)
        self.model = joblib.load("/app/seldon_model")

    def predict(self, user_ids, features_names):
        """
        Return a prediction.

        Parameters
        ----------
        X : array-like
        feature_names : array of feature names (optional)
        """
        print("Predict called")
        return self.model.predict(user_ids)
