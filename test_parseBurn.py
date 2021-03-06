from nose.tools import assert_equal, assert_true
import parseBurn
import datetime

def test_can_parse_kill():
    html = r'<div class="col-4"><div><a href="https://zkillboard.com/kill/38481364" target="_blank"><img class="img-circle" src="static/28844.png" width="150px"></a><h3>8,364,738,569 ISK</h3><p>2014-04-27 20:01:00<br><a href="https://zkillboard.com/kill/38481364" target="_blank">Nantik23 <p></p></a></p></div></div>'
    kills = parseBurn.parseHTML(html)
    assert_true(len(kills) > 0, 'no kills were parsed')
    assert_equal(u'https://zkillboard.com/kill/38481364', kills[0].link)
    assert_equal(8364738569, kills[0].amount)
    assert_equal('Nantik23', kills[0].name)

    #2014-04-27 20:01:00
    date = datetime.datetime(2014, 4, 27, 20, 01, 00) 
    assert_equal(date, kills[0].date)