const childProcess = require('child_process');
const fs = require('fs');
const { logger } = require('jege/server');
const path = require('path');

const paths = require('./paths');

const log = logger('[prototype]');
const WEBAPP_PACKAGE_NAME = 'webapp';

const latestCommitHash = (function getLastetCommitHash() {
  return childProcess.execSync(`git log --pretty=format:'%h' -n 1`).toString();
})();

const websitePackagePath = (function getWebsitePackagePath() {
  const _path = path.resolve(paths.root, 'packages', WEBAPP_PACKAGE_NAME);

  if (fs.existsSync(_path) === undefined) {
    throw new Error('website package is not present');
  }

  return _path;
})();

exports.get = function get() {
  const processEnv = {
    BUILD_PATH: paths.build,
    DIST_PATH: paths.dist,
    LATEST_COMMIT_HASH: latestCommitHash,
    ROOT_PATH: paths.root,
    WEBPACK_CONFIG_CLIENT_LOCAL_WEB: path.resolve(websitePackagePath, 'scripts/webpack/webpack.config.client.local.web'),
    WEBPACK_CONFIG_CLIENT_PROD_WEB: path.resolve(websitePackagePath, 'scripts/webpack/webpack.config.client.prod.web'),
    WEBPACK_CONFIG_CLIENT_WEB: path.resolve(websitePackagePath, 'scripts/webpack/webpack.config.client.web'),
    WEBPACK_CONFIG_SERVER_LOCAL: path.resolve(websitePackagePath, 'scripts/webpack/webpack.config.server.local'),
    WEBPACK_CONFIG_SERVER_PROD: path.resolve(websitePackagePath, 'scripts/webpack/webpack.config.server.prod'),
    WEBSITE_BUILD_PATH: path.resolve(websitePackagePath, '.build'),
    WEBSITE_DATA_PATH: path.resolve(websitePackagePath, 'data'),
    WEBSITE_GET_DATA_PATH: path.resolve(websitePackagePath, 'scripts/getData'),
    WEBSITE_PUBLIC_URL: 'xxx-not-defined',
    WEBSITE_SRC_PATH: path.resolve(websitePackagePath, 'src'),
  };

  let envString = '';
  Object.keys(processEnv)
    .forEach((envKey) => {
      envString += `${envKey}: ${processEnv[envKey]}, `;
    });
  log('env.get(): %s', envString);

  return processEnv;
};
