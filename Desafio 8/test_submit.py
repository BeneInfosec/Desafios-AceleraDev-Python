import yaml

from main import doc


document = yaml.load(doc)


def test_826():
    assert document.get('securitySchemes').get('JWT')


def test_1376():
    assert document.get('securitySchemes').get('JWT').get('description')


def test_1565():
    assert document.get('securitySchemes').get('JWT').get('type')


def test_1358():
    assert document.get('securitySchemes').get('JWT').get('describedBy')


def test_2725():
    assert document.get('securitySchemes').get('JWT').get('describedBy').get('headers')


def test_2655():
    assert document.get('securitySchemes').get('JWT').get('describedBy').get('headers').get('Authorization')


def test_2500():
    assert document.get('securitySchemes').get('JWT').get('describedBy').get('responses')


def test_2420():
    assert document.get('securitySchemes').get('JWT').get('describedBy').get('responses').get(401)


def test_1763():
    assert document.get('securitySchemes').get('JWT').get('settings')


def test_168():
    assert document.get('types').get('Auth')


def test_1523():
    assert document.get('types').get('Auth').get('type')


def test_1076():
    assert document.get('types').get('Auth').get('discriminator')


def test_1304():
    assert document.get('types').get('Auth').get('properties')


def test_2600():
    assert document.get('types').get('Auth').get('properties').get('token')


def test_296():
    assert document.get('types').get('Agent')


def test_1466():
    assert document.get('types').get('Agent').get('type')


def test_1076():
    assert document.get('types').get('Agent').get('discriminator')


def test_1271():
    assert document.get('types').get('Agent').get('properties')


def test_2365():
    assert document.get('types').get('Agent').get('properties').get('agent_id')


def test_2715():
    assert document.get('types').get('Agent').get('properties').get('user_id')


def test_2730():
    assert document.get('types').get('Agent').get('properties').get('name')


def test_2040():
    assert document.get('types').get('Agent').get('properties').get('status')


def test_2785():
    assert document.get('types').get('Agent').get('properties').get('environment')


def test_2810():
    assert document.get('types').get('Agent').get('properties').get('version')


def test_2895():
    assert document.get('types').get('Agent').get('properties').get('address')


def test_1394():
    assert document.get('types').get('Agent').get('example')


def test_2465():
    assert document.get('types').get('Agent').get('example').get('agent_id')


def test_2755():
    assert document.get('types').get('Agent').get('example').get('user_id')


def test_2730():
    assert document.get('types').get('Agent').get('example').get('name')


def test_2620():
    assert document.get('types').get('Agent').get('example').get('status')


def test_2340():
    assert document.get('types').get('Agent').get('example').get('environment')


def test_2070():
    assert document.get('types').get('Agent').get('example').get('version')


def test_2580():
    assert document.get('types').get('Agent').get('example').get('address')


def test_252():
    assert document.get('types').get('Event')


def test_1085():
    assert document.get('types').get('Event').get('type')


def test_1808():
    assert document.get('types').get('Event').get('discriminator')


def test_1781():
    assert document.get('types').get('Event').get('properties')


def test_2975():
    assert document.get('types').get('Event').get('properties').get('event_id')


def test_2160():
    assert document.get('types').get('Event').get('properties').get('agent_id')


def test_2200():
    assert document.get('types').get('Event').get('properties').get('level')


def test_2210():
    assert document.get('types').get('Event').get('properties').get('payload')


def test_2590():
    assert document.get('types').get('Event').get('properties').get('shelved')


def test_2015():
    assert document.get('types').get('Event').get('properties').get('date')


def test_1790():
    assert document.get('types').get('Event').get('example')


def test_2480():
    assert document.get('types').get('Event').get('example').get('event_id')


def test_2020():
    assert document.get('types').get('Event').get('example').get('agent_id')


def test_2830():
    assert document.get('types').get('Event').get('example').get('level')


def test_2765():
    assert document.get('types').get('Event').get('example').get('data')


def test_2055():
    assert document.get('types').get('Event').get('example').get('shelve')


def test_764():
    assert document.get('types').get('Group')


def test_1742():
    assert document.get('types').get('Group').get('type')


def test_1643():
    assert document.get('types').get('Group').get('discriminator')


def test_1790():
    assert document.get('types').get('Group').get('properties')


def test_2875():
    assert document.get('types').get('Group').get('properties').get('group_id')


def test_2015():
    assert document.get('types').get('Group').get('properties').get('name')


def test_1232():
    assert document.get('types').get('Group').get('example')


def test_2845():
    assert document.get('types').get('Group').get('example').get('group_id')


def test_2860():
    assert document.get('types').get('Group').get('example').get('name')


def test_502():
    assert document.get('types').get('User')


def test_1325():
    assert document.get('types').get('User').get('type')


def test_1670():
    assert document.get('types').get('User').get('discriminator')


def test_1091():
    assert document.get('types').get('User').get('properties')


def test_2455():
    assert document.get('types').get('User').get('properties').get('user_id')


def test_2975():
    assert document.get('types').get('User').get('properties').get('name')


def test_2230():
    assert document.get('types').get('User').get('properties').get('email')


def test_2880():
    assert document.get('types').get('User').get('properties').get('last_login')


def test_2670():
    assert document.get('types').get('User').get('properties').get('group_id')


def test_638():
    assert document.get('/auth/token').get('post')


def test_1358():
    assert document.get('/auth/token').get('post').get('description')


def test_1808():
    assert document.get('/auth/token').get('post').get('body')


def test_2365():
    assert document.get('/auth/token').get('post').get('body').get('application/json')


def test_2715():
    assert document.get('/auth/token').get('post').get('body').get('application/json').get('username')


def test_2310():
    assert document.get('/auth/token').get('post').get('body').get('application/json').get('password')


def test_1121():
    assert document.get('/auth/token').get('post').get('responses')


def test_2105():
    assert document.get('/auth/token').get('post').get('responses').get(201)


def test_2065():
    assert document.get('/auth/token').get('post').get('responses').get(201).get('body')


def test_2930():
    assert document.get('/auth/token').get('post').get('responses').get(400)


def test_2925():
    assert document.get('/auth/token').get('post').get('responses').get(400).get('body')


def test_746():
    assert document.get('/agents').get('post')


def test_1442():
    assert document.get('/agents').get('post').get('description')


def test_1826():
    assert document.get('/agents').get('post').get('securedBy')


def test_1382():
    assert document.get('/agents').get('post').get('body')


def test_2680():
    assert document.get('/agents').get('post').get('body').get('application/json')


def test_2755():
    assert document.get('/agents').get('post').get('body').get('application/json').get('properties')


def test_2290():
    assert document.get('/agents').get('post').get('body').get('application/json').get('example')


def test_1055():
    assert document.get('/agents').get('post').get('responses')


def test_2335():
    assert document.get('/agents').get('post').get('responses').get(201)


def test_2030():
    assert document.get('/agents').get('post').get('responses').get(201).get('body')


def test_2990():
    assert document.get('/agents').get('post').get('responses').get(401)


def test_2200():
    assert document.get('/agents').get('post').get('responses').get(401).get('body')


def test_916():
    assert document.get('/agents').get('get')


def test_1409():
    assert document.get('/agents').get('get').get('description')


def test_1757():
    assert document.get('/agents').get('get').get('securedBy')


def test_1292():
    assert document.get('/agents').get('get').get('responses')


def test_2530():
    assert document.get('/agents').get('get').get('responses').get(200)


def test_2140():
    assert document.get('/agents').get('get').get('responses').get(200).get('body')


def test_664():
    assert document.get('/agents').get('/{id}')


def test_1313():
    assert document.get('/agents').get('/{id}').get('get')


def test_2755():
    assert document.get('/agents').get('/{id}').get('get').get('description')


def test_2305():
    assert document.get('/agents').get('/{id}').get('get').get('securedBy')


def test_2775():
    assert document.get('/agents').get('/{id}').get('get').get('responses')


def test_2965():
    assert document.get('/agents').get('/{id}').get('get').get('responses').get(200)


def test_2060():
    assert document.get('/agents').get('/{id}').get('get').get('responses').get(401)


def test_2625():
    assert document.get('/agents').get('/{id}').get('get').get('responses').get(404)


def test_1295():
    assert document.get('/agents').get('/{id}').get('put')


def test_2855():
    assert document.get('/agents').get('/{id}').get('put').get('description')


def test_2555():
    assert document.get('/agents').get('/{id}').get('put').get('securedBy')


def test_2610():
    assert document.get('/agents').get('/{id}').get('put').get('responses')


def test_2800():
    assert document.get('/agents').get('/{id}').get('put').get('responses').get(200)


def test_2295():
    assert document.get('/agents').get('/{id}').get('put').get('responses').get(401)


def test_2800():
    assert document.get('/agents').get('/{id}').get('put').get('responses').get(404)


def test_1460():
    assert document.get('/agents').get('/{id}').get('delete')


def test_2745():
    assert document.get('/agents').get('/{id}').get('delete').get('description')


def test_2420():
    assert document.get('/agents').get('/{id}').get('delete').get('securedBy')


def test_2990():
    assert document.get('/agents').get('/{id}').get('delete').get('responses')


def test_2350():
    assert document.get('/agents').get('/{id}').get('delete').get('responses').get(200)


def test_2125():
    assert document.get('/agents').get('/{id}').get('delete').get('responses').get(401)


def test_2510():
    assert document.get('/agents').get('/{id}').get('delete').get('responses').get(404)


def test_934():
    assert document.get('/agents').get('/{id}/events')


def test_1130():
    assert document.get('/agents').get('/{id}/events').get('post')


def test_2520():
    assert document.get('/agents').get('/{id}/events').get('post').get('description')


def test_2810():
    assert document.get('/agents').get('/{id}/events').get('post').get('securedBy')


def test_2760():
    assert document.get('/agents').get('/{id}/events').get('post').get('body')


def test_2695():
    assert document.get('/agents').get('/{id}/events').get('post').get('body').get('application/json')


def test_2505():
    assert document.get('/agents').get('/{id}/events').get('post').get('body').get('responses')


def test_2645():
    assert document.get('/agents').get('/{id}/events').get('post').get('body').get(201)


def test_2185():
    assert document.get('/agents').get('/{id}/events').get('post').get('body').get(401)


def test_2580():
    assert document.get('/agents').get('/{id}/events').get('post').get('body').get(404)


def test_1148():
    assert document.get('/agents').get('/{id}/events').get('get')


def test_2780():
    assert document.get('/agents').get('/{id}/events').get('get').get('description')


def test_2805():
    assert document.get('/agents').get('/{id}/events').get('get').get('securedBy')


def test_2415():
    assert document.get('/agents').get('/{id}/events').get('get').get('responses')


def test_2010():
    assert document.get('/agents').get('/{id}/events').get('get').get('responses').get(200)


def test_2545():
    assert document.get('/agents').get('/{id}/events').get('get').get('responses').get(401)


def test_2700():
    assert document.get('/agents').get('/{id}/events').get('get').get('responses').get(404)


def test_1808():
    assert document.get('/agents').get('/{id}/events').get('put')


def test_2880():
    assert document.get('/agents').get('/{id}/events').get('put').get('description')


def test_2595():
    assert document.get('/agents').get('/{id}/events').get('put').get('securedBy')


def test_2575():
    assert document.get('/agents').get('/{id}/events').get('put').get('body')


def test_2680():
    assert document.get('/agents').get('/{id}/events').get('put').get('body').get('application/json')


def test_2035():
    assert document.get('/agents').get('/{id}/events').get('put').get('body').get(200)


def test_2855():
    assert document.get('/agents').get('/{id}/events').get('put').get('body').get(401)


def test_2450():
    assert document.get('/agents').get('/{id}/events').get('put').get('body').get(404)


def test_1064():
    assert document.get('/agents').get('/{id}/events').get('delete')


def test_2410():
    assert document.get('/agents').get('/{id}/events').get('delete').get('description')


def test_2445():
    assert document.get('/agents').get('/{id}/events').get('delete').get('securedBy')


def test_2760():
    assert document.get('/agents').get('/{id}/events').get('delete').get('body')


def test_2550():
    assert document.get('/agents').get('/{id}/events').get('delete').get('body').get('application/json')


def test_2420():
    assert document.get('/agents').get('/{id}/events').get('delete').get('body').get(200)


def test_2605():
    assert document.get('/agents').get('/{id}/events').get('delete').get('body').get(401)


def test_2130():
    assert document.get('/agents').get('/{id}/events').get('delete').get('body').get(404)


def test_486():
    assert document.get('/users').get('post')


def test_1172():
    assert document.get('/users').get('post').get('description')


def test_1835():
    assert document.get('/users').get('post').get('securedBy')


def test_1910():
    assert document.get('/users').get('post').get('body')


def test_2440():
    assert document.get('/users').get('post').get('body').get('application/json')


def test_2650():
    assert document.get('/users').get('post').get('body').get('application/json').get('properties')


def test_1610():
    assert document.get('/users').get('post').get('responses')


def test_2090():
    assert document.get('/users').get('post').get('responses').get(201)


def test_2025():
    assert document.get('/users').get('post').get('responses').get(201).get('body')


def test_2875():
    assert document.get('/users').get('post').get('responses').get(401)


def test_2775():
    assert document.get('/users').get('post').get('responses').get(401).get('body')


def test_62():
    assert document.get('/users').get('get')


def test_1160():
    assert document.get('/users').get('get').get('description')


def test_1013():
    assert document.get('/users').get('get').get('securedBy')


def test_1535():
    assert document.get('/users').get('get').get('responses')


def test_2125():
    assert document.get('/users').get('get').get('responses').get(200)


def test_2740():
    assert document.get('/users').get('get').get('responses').get(200).get('body')


def test_458():
    assert document.get('/users').get('/{id}')


def test_1841():
    assert document.get('/users').get('/{id}').get('get')


def test_2275():
    assert document.get('/users').get('/{id}').get('get').get('description')


def test_2520():
    assert document.get('/users').get('/{id}').get('get').get('securedBy')


def test_2425():
    assert document.get('/users').get('/{id}').get('get').get('responses')


def test_2505():
    assert document.get('/users').get('/{id}').get('get').get('responses').get(200)


def test_2115():
    assert document.get('/users').get('/{id}').get('get').get('responses').get(401)


def test_2300():
    assert document.get('/users').get('/{id}').get('get').get('responses').get(404)


def test_1229():
    assert document.get('/users').get('/{id}').get('put')


def test_2350():
    assert document.get('/users').get('/{id}').get('put').get('description')


def test_2935():
    assert document.get('/users').get('/{id}').get('put').get('securedBy')


def test_2205():
    assert document.get('/users').get('/{id}').get('put').get('responses')


def test_2130():
    assert document.get('/users').get('/{id}').get('put').get('responses').get(200)


def test_2470():
    assert document.get('/users').get('/{id}').get('put').get('responses').get(401)


def test_2940():
    assert document.get('/users').get('/{id}').get('put').get('responses').get(404)


def test_1535():
    assert document.get('/users').get('/{id}').get('delete')


def test_2565():
    assert document.get('/users').get('/{id}').get('delete').get('description')


def test_2860():
    assert document.get('/users').get('/{id}').get('delete').get('securedBy')


def test_2310():
    assert document.get('/users').get('/{id}').get('delete').get('responses')


def test_2335():
    assert document.get('/users').get('/{id}').get('delete').get('responses').get(200)


def test_2910():
    assert document.get('/users').get('/{id}').get('delete').get('responses').get(401)


def test_2225():
    assert document.get('/users').get('/{id}').get('delete').get('responses').get(404)


def test_442():
    assert document.get('/groups').get('post')


def test_1103():
    assert document.get('/groups').get('post').get('description')


def test_1676():
    assert document.get('/groups').get('post').get('securedBy')


def test_1523():
    assert document.get('/groups').get('post').get('body')


def test_2375():
    assert document.get('/groups').get('post').get('body').get('application/json')


def test_2865():
    assert document.get('/groups').get('post').get('body').get('application/json').get('properties')


def test_2380():
    assert document.get('/groups').get('post').get('body').get('application/json').get('example')


def test_1538():
    assert document.get('/groups').get('post').get('responses')


def test_2705():
    assert document.get('/groups').get('post').get('responses').get(201)


def test_2145():
    assert document.get('/groups').get('post').get('responses').get(201).get('body')


def test_2040():
    assert document.get('/groups').get('post').get('responses').get(401)


def test_458():
    assert document.get('/groups').get('get')


def test_1046():
    assert document.get('/groups').get('get').get('description')


def test_1457():
    assert document.get('/groups').get('get').get('securedBy')


def test_1757():
    assert document.get('/groups').get('get').get('responses')


def test_2900():
    assert document.get('/groups').get('get').get('responses').get(200)


def test_2710():
    assert document.get('/groups').get('get').get('responses').get(200).get('body')


def test_2070():
    assert document.get('/groups').get('get').get('responses').get(401)


def test_2970():
    assert document.get('/groups').get('get').get('responses').get(401).get('body')


def test_80():
    assert document.get('/groups').get('/{id}')


def test_1835():
    assert document.get('/groups').get('/{id}').get('get')


def test_2680():
    assert document.get('/groups').get('/{id}').get('get').get('description')


def test_2565():
    assert document.get('/groups').get('/{id}').get('get').get('securedBy')


def test_2080():
    assert document.get('/groups').get('/{id}').get('get').get('responses')


def test_2120():
    assert document.get('/groups').get('/{id}').get('get').get('responses').get(200)


def test_2250():
    assert document.get('/groups').get('/{id}').get('get').get('responses').get(401)


def test_2270():
    assert document.get('/groups').get('/{id}').get('get').get('responses').get(404)


def test_1904():
    assert document.get('/groups').get('/{id}').get('put')


def test_2130():
    assert document.get('/groups').get('/{id}').get('put').get('description')


def test_2630():
    assert document.get('/groups').get('/{id}').get('put').get('securedBy')


def test_2525():
    assert document.get('/groups').get('/{id}').get('put').get('responses')


def test_2405():
    assert document.get('/groups').get('/{id}').get('put').get('responses').get(200)


def test_2255():
    assert document.get('/groups').get('/{id}').get('put').get('responses').get(401)


def test_1577():
    assert document.get('/groups').get('/{id}').get('delete')


def test_2090():
    assert document.get('/groups').get('/{id}').get('delete').get('description')


def test_2960():
    assert document.get('/groups').get('/{id}').get('delete').get('securedBy')


def test_2260():
    assert document.get('/groups').get('/{id}').get('delete').get('responses')
