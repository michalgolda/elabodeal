const dsn = 'https://3785464099b948e18884fe59dfbc438e@o320975.ingest.sentry.io/5367878';
const isEnabled = true;
const env = process.env.NODE_ENV === 'production' ? 'production' : 'development';
const isDebug = env === 'development' ? true : false;

Sentry.init( {
    dsn: dsn,
    enabled: isEnabled,
    debug: isDebug,
    environment: env
} );