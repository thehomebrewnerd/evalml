
from evalml.utils import Logger


def test_logger_log(caplog):
    logger = Logger()
    logger.log('Test message')
    assert caplog.messages[0] == 'Test message\n'

    caplog.clear()
    logger = Logger()
    logger.log('Test message', new_line=False)
    assert caplog.messages[0] == 'Test message'

    caplog.clear()
    logger.log_title('Log title')
    out = caplog.text
    assert 'Log title' in out

    caplog.clear()
    logger.log_subtitle('Log subtitle')
    out = caplog.text
    assert 'Log subtitle' in out


def test_logger_warn(caplog, capsys):
    logger = Logger()
    logger.warn('Test message', stack_info=True)
    assert 'Test message' in caplog.messages[0]
    assert 'Stack (most recent call last):' in caplog.text
