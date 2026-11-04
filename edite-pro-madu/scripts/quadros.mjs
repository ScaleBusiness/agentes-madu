// Gera vários quadros de uma composição com um bundle só (conferência rápida da edição).
// Uso (na pasta do projeto Remotion): node quadros.mjs <IdDaComposicao> <pasta-saida> <escala> <quadro> [<quadro> ...]
// Em zsh, passe a lista de quadros por substituição de comando: $(python3 -c "...")  (variável não se divide em palavras).
import {bundle} from '@remotion/bundler';
import {renderStill, selectComposition} from '@remotion/renderer';
import path from 'node:path';
const [id, saida, escala, ...frames] = process.argv.slice(2);
const serveUrl = await bundle({entryPoint: path.resolve('src/index.jsx')});
const composition = await selectComposition({serveUrl, id});
for (const f of frames) {
  await renderStill({serveUrl, composition, frame: Number(f), output: `${saida}/q-${String(f).padStart(4, '0')}.jpg`,
    imageFormat: 'jpeg', jpegQuality: 80, scale: Number(escala)});
}
console.log('ok', frames.length);
