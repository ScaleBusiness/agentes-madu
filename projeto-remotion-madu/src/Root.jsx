import React from 'react';
import {Composition} from 'remotion';

import {MaduAcolher, DURACAO_MADU_ACOLHER} from './edite/madu-acolher/MaduAcolher.jsx';
import {CapaMaduAcolher} from './edite/madu-acolher/CapaMaduAcolher.jsx';
import DADOS_MADU_ACOLHER_1X from './edite/madu-acolher/dados-madu-acolher.json';

import {MaduAcolher2, DURACAO_MADU_ACOLHER2} from './edite/madu-acolher2/MaduAcolher2.jsx';
import {CapaMaduAcolher2} from './edite/madu-acolher2/CapaMaduAcolher2.jsx';
import DADOS_MADU_ACOLHER2_1X from './edite/madu-acolher2/dados-madu-acolher2.json';

import {MaduSoneca, DURACAO_MADU_SONECA} from './edite/madu-soneca/MaduSoneca.jsx';
import {CapaMaduSoneca} from './edite/madu-soneca/CapaMaduSoneca.jsx';
import DADOS_MADU_SONECA_1X from './edite/madu-soneca/dados-madu-soneca.json';

import {MaduAjuda3h, DURACAO_MADU_AJUDA} from './edite/madu-ajuda-3h/MaduAjuda3h.jsx';
import {CapaMaduAjuda3h} from './edite/madu-ajuda-3h/CapaMaduAjuda3h.jsx';
import DADOS_MADU_AJUDA_1X from './edite/madu-ajuda-3h/dados-madu-ajuda-3h.json';

import {MaduDespertar, DURACAO_MADU_DESPERTAR} from './edite/madu-despertar/MaduDespertar.jsx';
import {CapaMaduDespertar} from './edite/madu-despertar/CapaMaduDespertar.jsx';
import DADOS_MADU_DESPERTAR_1X from './edite/madu-despertar/dados-madu-despertar.json';

import {MaduPeito, DURACAO_MADU_PEITO} from './edite/madu-peito/MaduPeito.jsx';
import {CapaMaduPeito} from './edite/madu-peito/CapaMaduPeito.jsx';
import DADOS_MADU_PEITO_1X from './edite/madu-peito/dados-madu-peito.json';

import {MaduAutonomia, DURACAO_MADU_AUTONOMIA} from './edite/madu-autonomia/MaduAutonomia.jsx';
import {CapaMaduAutonomia} from './edite/madu-autonomia/CapaMaduAutonomia.jsx';
import DADOS_MADU_AUTONOMIA_1X from './edite/madu-autonomia/dados-madu-autonomia.json';

import {MaduSoltos, DURACAO_MADU_SOLTOS} from './edite/madu-soltos/MaduSoltos.jsx';
import {CapaMaduSoltos} from './edite/madu-soltos/CapaMaduSoltos.jsx';
import DADOS_MADU_SOLTOS_1X from './edite/madu-soltos/dados-madu-soltos.json';

const acelera = (d, v) => ({
  duracao: d.duracao / v,
  cortes: d.cortes.map((c) => ({...c, video: c.video.replace('.mp4', `-x${v}.mp4`), de: c.de / v, ate: c.ate / v, saida: c.saida / v})),
  grupos: d.grupos.map((g) => ({...g, inicio: g.inicio / v, fim: g.fim / v,
    palavras: g.palavras.map((w) => ({...w, inicio: w.inicio / v, fim: w.fim / v}))})),
});

const aceleraPorTake = (d, porTake, padrao) => {
  let acc = 0;
  const mapa = d.cortes.map((c) => {
    const take = (c.video.match(/take-(\d+)/) || [])[1];
    const v = porTake[take] || padrao;
    const dur = (c.ate - c.de) / v;
    const r = {de1: c.saida, fim1: c.saida + (c.ate - c.de), v, saida: acc};
    acc += dur;
    return {r, corte: {...c, video: c.video.replace('.mp4', `-x${v}.mp4`), de: c.de / v, ate: c.ate / v, saida: r.saida}};
  });
  const t = (x) => {
    const m = mapa.find(({r}) => x < r.fim1 + 1e-6) || mapa[mapa.length - 1];
    return m.r.saida + (Math.min(x, m.r.fim1) - m.r.de1) / m.r.v;
  };
  return {
    duracao: acc,
    cortes: mapa.map((m) => m.corte),
    grupos: d.grupos.map((g) => ({...g, inicio: t(g.inicio), fim: t(g.fim),
      palavras: g.palavras.map((w) => ({...w, inicio: t(w.inicio), fim: t(w.fim)}))})),
  };
};

const DADOS_MADU_ACOLHER = acelera(DADOS_MADU_ACOLHER_1X, 1.3);
const DADOS_MADU_ACOLHER2 = acelera(DADOS_MADU_ACOLHER2_1X, 1.3);
const DADOS_MADU_SONECA = acelera(DADOS_MADU_SONECA_1X, 1.3);
const DADOS_MADU_AJUDA = acelera(DADOS_MADU_AJUDA_1X, 1.3);
const DADOS_MADU_DESPERTAR = aceleraPorTake(DADOS_MADU_DESPERTAR_1X, {'9279': 1.1}, 1.3);
const DADOS_MADU_PEITO = acelera(DADOS_MADU_PEITO_1X, 1.3);
const DADOS_MADU_AUTONOMIA = acelera(DADOS_MADU_AUTONOMIA_1X, 1.3);
const DADOS_MADU_SOLTOS = acelera(DADOS_MADU_SOLTOS_1X, 1.3);

export const Root = () => (
  <>
    <Composition id="MaduAcolher" component={MaduAcolher} durationInFrames={Math.round(DURACAO_MADU_ACOLHER(DADOS_MADU_ACOLHER) * 30)} fps={30} width={1080} height={1920} defaultProps={{dados: DADOS_MADU_ACOLHER}} />
    <Composition id="CapaMaduAcolher" component={CapaMaduAcolher} durationInFrames={1} fps={30} width={1080} height={1920} />
    <Composition id="MaduAcolher2" component={MaduAcolher2} durationInFrames={Math.round(DURACAO_MADU_ACOLHER2(DADOS_MADU_ACOLHER2) * 30)} fps={30} width={1080} height={1920} defaultProps={{dados: DADOS_MADU_ACOLHER2}} />
    <Composition id="CapaMaduAcolher2" component={CapaMaduAcolher2} durationInFrames={1} fps={30} width={1080} height={1920} />
    <Composition id="MaduSoneca" component={MaduSoneca} durationInFrames={Math.round(DURACAO_MADU_SONECA(DADOS_MADU_SONECA) * 30)} fps={30} width={1080} height={1920} defaultProps={{dados: DADOS_MADU_SONECA}} />
    <Composition id="CapaMaduSoneca" component={CapaMaduSoneca} durationInFrames={1} fps={30} width={1080} height={1920} />
    <Composition id="MaduAjuda3h" component={MaduAjuda3h} durationInFrames={Math.round(DURACAO_MADU_AJUDA(DADOS_MADU_AJUDA) * 30)} fps={30} width={1080} height={1920} defaultProps={{dados: DADOS_MADU_AJUDA}} />
    <Composition id="CapaMaduAjuda3h" component={CapaMaduAjuda3h} durationInFrames={1} fps={30} width={1080} height={1920} />
    <Composition id="MaduDespertar" component={MaduDespertar} durationInFrames={Math.round(DURACAO_MADU_DESPERTAR(DADOS_MADU_DESPERTAR) * 30)} fps={30} width={1080} height={1920} defaultProps={{dados: DADOS_MADU_DESPERTAR}} />
    <Composition id="CapaMaduDespertar" component={CapaMaduDespertar} durationInFrames={1} fps={30} width={1080} height={1920} />
    <Composition id="MaduPeito" component={MaduPeito} durationInFrames={Math.round(DURACAO_MADU_PEITO(DADOS_MADU_PEITO) * 30)} fps={30} width={1080} height={1920} defaultProps={{dados: DADOS_MADU_PEITO}} />
    <Composition id="CapaMaduPeito" component={CapaMaduPeito} durationInFrames={1} fps={30} width={1080} height={1920} />
    <Composition id="MaduAutonomia" component={MaduAutonomia} durationInFrames={Math.round(DURACAO_MADU_AUTONOMIA(DADOS_MADU_AUTONOMIA) * 30)} fps={30} width={1080} height={1920} defaultProps={{dados: DADOS_MADU_AUTONOMIA}} />
    <Composition id="CapaMaduAutonomia" component={CapaMaduAutonomia} durationInFrames={1} fps={30} width={1080} height={1920} />
    <Composition id="MaduSoltos" component={MaduSoltos} durationInFrames={Math.round(DURACAO_MADU_SOLTOS(DADOS_MADU_SOLTOS) * 30)} fps={30} width={1080} height={1920} defaultProps={{dados: DADOS_MADU_SOLTOS}} />
    <Composition id="CapaMaduSoltos" component={CapaMaduSoltos} durationInFrames={1} fps={30} width={1080} height={1920} />
  </>
);
