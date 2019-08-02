from series_tiempo_ar_api.apps.api.helpers import get_periodicity_human_format
from series_tiempo_ar_api.apps.management import meta_keys


class SeriesQuery:

    def __init__(self, field_model, rep_mode):
        self.field_model = field_model
        self.rep_mode = rep_mode

    def periodicity(self):
        serie_periodicity = meta_keys.get(self.field_model, meta_keys.PERIODICITY)
        distribution_periodicity = meta_keys.get(self.field_model.distribution, meta_keys.PERIODICITY)
        return get_periodicity_human_format(serie_periodicity or distribution_periodicity)
