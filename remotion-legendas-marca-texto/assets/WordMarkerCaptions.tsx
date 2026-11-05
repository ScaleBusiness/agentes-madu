import {interpolate, useCurrentFrame, useVideoConfig} from "remotion";

export type MarkedWord = {text: string; startMs: number; endMs: number; emphasis?: boolean};
export type CaptionPage = {startMs: number; endMs: number; words: MarkedWord[]};

/** Highlight uses measured speech timestamps; pauses have no highlighted word. */
export const WordMarkerCaptions = ({pages}: {pages: CaptionPage[]}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const time = frame * 1000 / fps;
  const page = pages.find((item) => time >= item.startMs && time < item.endMs);
  if (!page) return null;
  return <div style={{position: "absolute", left: 84, right: 134, top: 1450, textAlign: "center", color: "#1F4B7A", fontFamily: "MaduInter", fontWeight: 800, fontSize: 66, lineHeight: "102px", letterSpacing: -1.6}}>
    {page.words.map((word, index) => {
      const active = time >= word.startMs && time < word.endMs;
      return <span key={index} style={{display: "inline-block", position: "relative", margin: "0 7px", padding: "0 5px", whiteSpace: "nowrap", fontFamily: word.emphasis ? "MaduPlayfair" : "MaduInter", fontWeight: word.emphasis ? 400 : 800, fontStyle: word.emphasis ? "italic" : "normal", fontSize: word.emphasis ? 82 : 66, verticalAlign: "baseline"}}>
        <span style={{position: "absolute", inset: "17px -3px 9px", backgroundColor: "#FFDBD5", borderRadius: 5, rotate: "-1.3deg", opacity: active ? interpolate(time-word.startMs,[0,45],[.65,1],{extrapolateLeft:"clamp",extrapolateRight:"clamp"}) : 0}} />
        <span style={{position:"relative"}}>{word.text}</span>
      </span>;
    })}
  </div>;
};
