import React from "react";
const Section : React.FC<React.PropsWithChildren> = ({children}) => {
  return <section className="section">{children}</section>
}

export default Section;
