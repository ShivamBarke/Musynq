import React from "react";
import styled from 'styled-components';
import { BrandLogo } from "../../components/brandLogo";
import { Button } from "../../components/button";
import TopSectionBackgroundImg from "../../images/bg1.jpg";
import listen from "../../images/listen.png";
import {Marginer} from "../../components/marginer";

const TopSectionContainer = styled.div`
    width: 100%;
    height: 790px;
    background: url(${TopSectionBackgroundImg});
    background-position: 0px -170px;
    background-size: cover;

`;

const BackgroundFilter = styled.div`
    width: 100%;
    height: 100%;
    background-color: rgba(255, 102, 0, 0.7);
    display: flex:
    flex-direction:column;
`;

const TopSectionInnerContainer = styled.div`
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: space-evenly;

`;

const StandoutImage = styled.div`
    width: 40em;
    height: 28em;

    img {
        width: 100%;
        height: 100%;
    }
`;

const LogoContainer = styled.div`
    display: flex;
    align-items: center;
    flex-direction: column;
    padding-left: 100px;
`;

const SloganText = styled.h3`
    margin: 0;
    line-height: 1.4;
    color: #000;
    font-weight: 600;
    font-size: 30px;
    
    

`;


export function TopSection(props) {
    const { children } = props;

    return <TopSectionContainer>
        <BackgroundFilter>
            {children}
            <TopSectionInnerContainer>
                <LogoContainer>
                    <BrandLogo logoSize={400}/>
                    <Marginer direction="vertical" margin={5}/>
                    <SloganText>For You, By You</SloganText>
                    <Marginer direction="vertical" margin={15}/>
                    <Button>FIND YOUR MUSIC</Button>
                </LogoContainer>
                <StandoutImage>
                    <img src= {listen} alt="listen"/>
                </StandoutImage>
                
            </TopSectionInnerContainer>
        </BackgroundFilter>
    </TopSectionContainer>
}