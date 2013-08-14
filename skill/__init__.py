from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    # Use mako as default renderer
    config.add_renderer(name='.html', factory="pyramid.mako_templating.renderer_factory")
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('experiment', '/experiment/{case}')
    config.add_route('image', '/image/{id}')
    config.add_route('detail', '/detail/{case}/{quantity}/{period}')
    config.scan()
    return config.make_wsgi_app()
