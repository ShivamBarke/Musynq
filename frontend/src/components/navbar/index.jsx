import React from "react";
import styled from "styled-components";
import { BrandLogo } from "../brandLogo";
import { Button } from "../button";
import { Marginer } from "../marginer";



const NavbarContainer = styled.div`
    width: 100%;
    height: 100px;
    
    justify-content: space-between;
    display: flex;
    padding: 0.5em 2em;

`;
const AccessabilityContainer = styled.div`
    height: 100%;
    display: flex;
    align-items: center;
`
const AnchorLink = styled.a`
    font-size: 25px;
    color: #fff;
    cursor: pointer;
    text-decoration;
    outline: none;
    transition: all 200ms ease-in-out;

    &:hover {
        filter: contrast(0.6);
    }
`;
const Seperator = styled.div`
    height: 40%;
    width: 1px;
    width: 1px;
    background-color: #fff;
`;

export function Navbar(props) {
   
    return (
        <NavbarContainer>
          <BrandLogo/>
          <AccessabilityContainer>
              <AnchorLink>LOGIN</AnchorLink>
              <Marginer direction="horizontal" margin={15}/>
              <Seperator/>
              <Marginer direction="horizontal" margin={15}/>
              <Button size={23}>REGISTER</Button>
          </AccessabilityContainer>
        </NavbarContainer>
    );
}