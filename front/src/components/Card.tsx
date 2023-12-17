import React from "react";
const Card : React.FC<React.PropsWithChildren> = ({children}) => {
  return <div className="card">{children}</div>
}

export default Card;
