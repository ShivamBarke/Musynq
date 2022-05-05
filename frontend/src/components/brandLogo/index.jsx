import React from "react";
import styled from "styled-components";
import LogoImg from "../../images/logo.png";

const BrandLogoContainer = styled.div`
    display: flex;
    align-items: center;
`;

const LogoImage = styled.div`
    widht: ${({size}) => size ? size + "px" : "5em"};
    height: ${({size}) => size ? size + "px" : "5em"};

    img {
        width: 100%;
        height: 100%;
    }
`;
export function BrandLogo(props) {
    const { logoSize } = props;

    return <BrandLogoContainer>
        <LogoImage size={logoSize}>
            <img src={LogoImg} alt="musync logo"/>
        </LogoImage>
    </BrandLogoContainer>
}