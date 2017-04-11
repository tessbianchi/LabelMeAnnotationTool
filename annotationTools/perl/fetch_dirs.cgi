#!/usr/bin/perl

require 'globalvariables.pl';
# require 'logfile_helper.pl';
use vars qw($LM_HOME);

print "Content-type: text/xml\n\n" ;

use warnings;
use strict;
use File::Find;

my $fname = $LM_HOME . "Images";

my $dir = shift || $fname;

find \&by_extension, $dir;

sub by_extension {
    return if /^\./;                    # skip dotfiles
    return unless -f;                   # skip non-files
    return unless /\.([^.]+)$/;         # skip if no filename extension
    my $ext = lc $1;                    # ignore case
    $File::Find::name =~ s#^\Q$dir/##;  # trim starting directory name
    print $File::Find::name;
    print " "
}

