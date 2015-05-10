Feature: competing AtCoder

  Scenario Outline: solve probrem
    Given I have a <sample>
    When I run the main program
    Then I get output files
    And the output files are same as expected files

    Examples: samples
    | sample  |
    | sample1 |
    | sample2 |

  
