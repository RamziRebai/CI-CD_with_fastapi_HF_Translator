from app.main import predict


def test_func():
    assert type(predict("Machine learning is great, isn't it?")) == str
