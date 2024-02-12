import typescript from '@rollup/plugin-typescript';
import copy from 'rollup-plugin-copy';

export default {
  input: ['./src/index.ts', './src/providers/openai.ts', './src/providers/wolframalpha.ts'],
  output: {
    dir: './dist/js',
    format: 'esm'
  },
  plugins: [
    typescript(),
    copy({
      targets: [
        { src: './public/index.html', dest: 'dist' }
      ]
    })
  ]
};
