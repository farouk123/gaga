import os
import sys
import bottle

@bottle.route('/')
def index():
    pyver = '.'.join(map(str, tuple(sys.version_info)[:3]))
    return 'جامعة العلوم والتقانة-كلية الحاسوب وتقانة المعلزمات-ماجستير نظم المعلومات-محمد فاروق! (from <b>Python %s</b>)' % (pyver,)


application = bottle.default_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', '8000'))
    bottle.run(host='0.0.0.0', port=port)

