import React from "react";
import styled from "styled-components";

const ButtonWrapper = styled.button`
    
    border: 0;
    outline: 1;
    color: #fff;
    padding: 5px;
    font-size: ${({ size }) => size ? size + "px" : "28px" };
    font-weight: 500;
    border-radius: 8px;
    background-color:#ffbb00;
    font-family:'Quicksand';
    
    cursor: pointer;
    transition: all 200ms ease-in-out;
    
    &:hover{
        background-color:#ff9900;
    }
    &:focus {
        outline: none;
    }
    
`;

export function Button(props) {
    const { size } = props;
    return<ButtonWrapper size={size}>{props.children}</ButtonWrapper>

}