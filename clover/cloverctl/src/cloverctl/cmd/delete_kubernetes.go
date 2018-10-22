// Copyright (c) Authors of Clover
//
// All rights reserved. This program and the accompanying materials
// are made available under the terms of the Apache License, Version 2.0
// which accompanies this distribution, and is available at
// http://www.apache.org/licenses/LICENSE-2.0

package cmd

import (
    "fmt"
    "encoding/json"

    "gopkg.in/resty.v1"
    "github.com/spf13/cobra"
)

var name string
var delkubeproviderCmd = &cobra.Command{
    Use:   "kubernetes",
    Short: "delete one kubernete provider by name from spinnaker",
    Long: ``,
    Run: func(cmd *cobra.Command, args []string) {
        delProvider()
    },
}

func init() {
    providerdelCmd.AddCommand(delkubeproviderCmd)
    delkubeproviderCmd.Flags().StringVarP(&name, "name", "n", "", "Input kubernetes account name")
    delkubeproviderCmd.MarkFlagRequired("name")

}

func delProvider() {
    url := controllerIP + "/halyard/delprovider"

    var in = map[string]string{"name": name, "provider":"kubernetes"}
    out_json, err := json.Marshal(in)
    if err != nil {
        fmt.Println("json.Marshal failed:", err)
        return
    }
    resp, err := resty.R().
    SetHeader("Content-Type", "application/json").
    SetBody(out_json).
    Post(url)
    if err != nil {
        panic(err.Error())
    }
    fmt.Printf("\n%v\n", resp)

}