const env = require('./env');

const processEnv = env.get();

const { argv } = require('yargs');
const { createLauncher, proc } = require('process-launch');
const { logger } = require('jege/server');

const log = logger('[prototype]');

const processDefinitions = {
  webappDev: proc(
    'node',
    [
      './scripts/launch.js',
      ...argv._,
    ],
    {
      cwd: `./packages/webapp`,
      env: {
        NODE_ENV: 'development',
        ...processEnv,
      },
      stdio: 'inherit',
    },
  ),
  webappEject: proc(
    'node',
    [
      './scripts/launch.js',
      ...argv._,
    ],
    {
      cwd: `./packages/webapp`,
      env: {
        NODE_ENV: 'production',
        ...processEnv,
      },
      stdio: 'inherit',
    },
  ),
};

const processGroupDefinitions = {
  default: ['webappDev'],
};

function launcher() {
  try {
    log('launcher(): argv: %j', argv);

    const Launcher = createLauncher({
      processDefinitions,
      processGroupDefinitions,
    });

    Launcher.run({
      process: argv.process,
      processGroup: argv.processGroup,
    });
  } catch (err) {
    log('launcher(): Error reading file', err);
  }
}

module.exports = launcher;

if (require.main === module) {
  launcher();
}
