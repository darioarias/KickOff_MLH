import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

lstm_finance_runner = bentoml.keras.get('lstm_finance:latest').to_runner()

svc = bentoml.Service("stock_prediction", runners=[lstm_finance_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def predict(input_series: np.ndarray) -> np.ndarray:
    result = lstm_finance_runner.predict.run(input_series)
    return result