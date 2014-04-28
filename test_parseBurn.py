from nose.tools import assert_equal, assert_true
import parseBurn

def test_can_parse_kill():
    html = r'<div class="col-4"><div><a href="https://zkillboard.com/kill/38481364" target="_blank"><img class="img-circle" src="static/28844.png" width="150px"></a><h3>8,364,738,569 ISK</h3><p>2014-04-27 20:01:00<br><a href="https://zkillboard.com/kill/38481364" target="_blank">Nantik23 <p></p></a></p></div></div>'
    kills = parseBurn.parseBurn(html)
    print kills
    assert_true(len(kills) > 0, 'no kills were parsed')
    assert_equal(u'https://zkillboard.com/kill/38481364', kills[0].link)