import { env } from 'process';

import * as Sentry from "@sentry/browser";
import { Integrations } from "@sentry/tracing";


Sentry.init(	{
  dsn: "https://3785464099b948e18884fe59dfbc438e@o320975.ingest.sentry.io/5367878",
  integrations: [ new Integrations.BrowserTracing() ],
  debug: env.NODE_ENV === 'production' ? false : true
}	);

import './nav.js';
import './payment.js';
import './scrollup.js';
import './share-cart.js';
import './update-product.js';
import './delivery-form.js';
import './product-detail.js';
import './cart-add-popup.js';
import './change-review-product-popup.js';
import './review-product-popup.js';
import './add-product.js';