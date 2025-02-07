const packageInfo = require('../package.json');

module.exports = {
  openapi: '3.0.0',
  info: {
    title: 'SAML Jackson API',
    version: packageInfo.version,
    description: 'This is the API documentation for SAML Jackson service.',
    termsOfService: 'https://boxyhq.com/terms.html',
    contact: {
      name: 'Boxy HQ',
      url: 'https://boxyhq.com/',
      email: 'support@boxyhq.com',
    },
    license: {
      name: 'Apache-2.0 License',
      url: 'https://github.com/boxyhq/jackson/blob/main/LICENSE',
    },
  },
  host: 'localhost:5225',
  basePath: '/',
  schemes: ['http', 'https'],
  securityDefinitions: {
    apiKey: {
      type: 'apiKey',
      in: 'header',
      name: 'Authorization',
    },
  },
  security: [
    {
      apiKey: [],
    },
  ],
};
