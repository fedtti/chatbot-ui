import dotenv from 'dotenv';
import typescript from '@rollup/plugin-typescript';
import copy from 'rollup-plugin-copy';

dotenv.config();

export default {
  input: ['./src/client.ts', './src/server.ts'],
  output: {
    dir: './dist/js',
    format: 'esm'
  },
  plugins: [
    typescript(),
    copy({
      targets: [
        { src: './public/index.html', dest: './dist' },
        { src: './public/css/main.css', dest: './dist/css' },
        { src: './public/img/bot.svg', dest: './dist/img' }
      ]
    })
  ]
};
