import pandas as pd


class DistributionCsvReader:

    def __init__(self, distribution, index_col):
        self.distribution = distribution
        self.index_col = index_col

    def read(self):
        url = self.distribution.data_file
        if url is None:
            raise ValueError

        try:
            return self.read_csv_with_encoding(url, 'utf-8')
        except UnicodeDecodeError:
            return self.read_csv_with_encoding(url, 'latin1')

    def read_csv_with_encoding(self, data_file, encoding):
        return pd.read_csv(data_file,
                           parse_dates=[self.index_col],
                           index_col=self.index_col,
                           encoding=encoding)
